#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:         BO ZENG
Created:        Monday November 20 12:33:08 2017
Operation system required: Linux (currently not available for windows)
Dependencies:   Python 3.5
                numpy
                Bio
                freecontact (currently only availble in linux)
                pandas
Purpose:        Self-interacting single-pass membrane protein interface residues prediction

"""
# I'm getting sick of the warnings that occur due to imported seaborn and statsmodels.stats.api modules, and have nothing to do with your code.
# you should turn on warnings once a month to check if there is anything related to your code
#import warnings
#warnings.filterwarnings("ignore")

import argparse
import os
import platform
import sys
import pandas as pd
import thoipapy

parser = argparse.ArgumentParser()

parser.add_argument("-s",  # "-settingsfile",
                    help=r'Full path to your excel settings file.'
                         r'E.g. "\Path\to\your\settingsfile.xlsx"')

if __name__ == "__main__":
    sys.stdout.write('\nRun thoipapy as follows:')
    sys.stdout.write(r'python \Path\to\run.py -s \Path\to\your\settingsfile.xlsx')
    # get the command-line arguments
    args = parser.parse_args()
    # args.s is the excel_settings_file input by the user
    s = thoipapy.common.create_settingdict(args.s)

    ##############################################################################################
    #                                                                                            #
    #                               setname, logging, results folder                             #
    #                                                                                            #
    ##############################################################################################
    sets_folder = os.path.join(s["dropbox_dir"], "sets")

    # if multiple sets need to be run, split them by comma
    if isinstance(s["set_number"], str) and "," in s["set_number"]:
        list_protein_sets = [int(n) for n in s["set_number"].split(",")]
    else:
        list_protein_sets = [s["set_number"]]

    for set_number in list_protein_sets:
        s["set_number"] = set_number
        # define set name, which should be in the excel file name
        setname = "set{:02d}".format(s["set_number"])
        # add to the dictionary itself
        s["setname"] = setname
        # create a results folder for that set
        if not os.path.isdir(os.path.join(s["thoipapy_data_folder"], "Results", setname)):
            os.makedirs(os.path.join(s["thoipapy_data_folder"], "Results", setname))

        logging = thoipapy.common.setup_keyboard_interrupt_and_error_logging(s, setname)
        logging.info("STARTING PROCESSING OF {}.".format(setname))

        set_path = thoipapy.common.get_path_of_protein_set(setname, sets_folder)

        ##############################################################################################
        #                                                                                            #
        #                     open and process a set of protein sequences                            #
        #                                                                                            #
        ##############################################################################################
        # load the protein set (e.g. set01.xlsx) as a dataframe
        df_set = pd.read_excel(set_path, sheetname='proteins')

        # create list of uniprot accessions to run
        acc_list = df_set.acc.tolist()
        sys.stdout.write("settings file : {}\nsettings : {}\nprotein set number {}, acc_list : {}\n".format(os.path.basename(args.s), s, s["set_number"], acc_list))
        sys.stdout.flush()

        dfset = thoipapy.common.process_set_protein_seqs(s, setname, df_set, set_path)

        # create a database label. Either crystal, NMR, ETRA or "mixed"
        unique_database_labels = df_set["database"].unique()
        if len(unique_database_labels.shape) == 1:
            database_for_full_set = unique_database_labels[0]
        else:
            database_for_full_set = "mixed"

        ###################################################################################################
        #                                                                                                 #
        #                  calculate closedistance from NMR and crystal structures                        #
        #                                                                                                 #
        ###################################################################################################

        # DEPRECATED. Use atom_dist module instead to get closest heavy-atom distances
        # if s["Get_Tmd_Homodimers"] :
        #     #thoipapy.structures.deprecated.get_tmd_nr_homodimer.download_xml_get_alphahelix_get_homo_pair(s, logging)
        #     #thoipapy.structures.deprecated.get_tmd_nr_homodimer.Download_trpdb_Calc_inter_rr_pairs(s, logging)
        #     #thoipapy.structures.deprecated.get_tmd_nr_homodimer.create_redundant_interact_homodimer_rm_shorttm(s, logging)
        #     #thoipapy.structures.deprecated.get_tmd_nr_homodimer.extract_crystal_resolv035_interact_pairs_and_create_fasta_file(s, logging)
        #     thoipapy.structures.deprecated.get_tmd_nr_homodimer.create_multiple_bind_closedist_file(s, logging)
        #     pass

        if s["retrospective_coevolution"]:
            #thoipapy.figs.retrospective.calc_retrospective_coev_from_list_interf_res(s, dfset, logging)
            thoipapy.figs.retrospective.calc_retrospective_coev_from_struct_contacts(s, dfset, logging)

        #if s["calc_NMR_closedist"] :
        #    thoipapy.structures.deprecated.NMR_data.calc_closedist_from_NMR_best_model(s)

        if s["Atom_Close_Dist"]:
            infor = thoipapy.closest_heavy_atom_dist.homodimer_residue_closedist_calculate_from_complex(thoipapy, s, logging)
            sys.stdout.write(infor)

        ###################################################################################################
        #                                                                                                 #
        #                   homologues download from NCBI. parse, filter and save                         #
        #                                                                                                 #
        ###################################################################################################

        if s["run_retrieve_NCBI_homologues_with_blastp"]:
            thoipapy.homologues.NCBI_download.download_homologues_from_ncbi_mult_prot(s, df_set, logging)

        if s["run_parse_homologues_xml_into_csv"]:
            thoipapy.homologues.NCBI_parser.parse_NCBI_xml_to_csv_mult_prot(s, df_set, logging)

        if s["parse_csv_homologues_to_alignment"]:
            thoipapy.homologues.NCBI_parser.extract_filtered_csv_homologues_to_alignments_mult_prot(s, df_set, logging)


        ###################################################################################################
        #                                                                                                 #
        #                   machine learning feature calculation                                             #
        #                                                                                                 #
        ###################################################################################################

        if s["pssm_feature_calculation"]:
            thoipapy.residue_properties.create_PSSM_from_MSA_mult_prot(s, df_set, logging)

        if s["entropy_feature_calculation"]:
            thoipapy.residue_properties.entropy_calculation_mult_prot(s, df_set, logging)

        if s["cumulative_coevolution_feature_calculation"]:
            if "Windows" in platform.system():
                sys.stdout.write("\n Freecontact cannot be run in Windows! Skipping coevolution_calculation_with_freecontact_mult_prot.")
                thoipapy.residue_properties.parse_freecontact_coevolution_mult_prot(s, df_set, logging)
            else:
                thoipapy.residue_properties.coevolution_calculation_with_freecontact_mult_prot(s, df_set, logging)
                thoipapy.residue_properties.parse_freecontact_coevolution_mult_prot(s, df_set, logging)

        if s["clac_relative_position"]:
            thoipapy.residue_properties.calc_relative_position_mult_prot(s, df_set, logging)

        if s["calc_lipo_from_pssm"]:
            thoipapy.residue_properties.lipo_from_pssm_mult_prot(s, df_set, logging)

        if s["lips_score_feature_calculation"]:
            thoipapy.residue_properties.LIPS_score_calculation_mult_prot(s, df_set, logging)
            thoipapy.residue_properties.parse_LIPS_score_mult_prot(s, df_set, logging)

        if s["motifs_from_seq"]:
            thoipapy.residue_properties.motifs_from_seq_mult_protein(s, df_set, logging)

        if s["combine_feature_into_train_data"]:
            thoipapy.residue_properties.combine_all_features_mult_prot(s, df_set, logging)
            thoipapy.residue_properties.add_physical_parameters_to_features_mult_prot(s, df_set, logging)
            thoipapy.residue_properties.add_experimental_data_to_combined_features_mult_prot(s, df_set, logging)
            if s["generate_randomised_interfaces"]:
                thoipapy.residue_properties.add_random_interface_to_combined_features_mult_prot(s, df_set, logging)
            if "add_PREDDIMER_TMDOCK_to_combined_features" in s:
                if s["add_PREDDIMER_TMDOCK_to_combined_features"]:
                    thoipapy.residue_properties.add_PREDDIMER_TMDOCK_to_combined_features_mult_prot(s, df_set, logging)
            if s["remove_crystal_hetero"]:
                thoipapy.residue_properties.remove_crystal_hetero_contact_residues_mult_prot(s, df_set, logging)
            thoipapy.residue_properties.combine_all_train_data_for_machine_learning(s, df_set, logging)

        ###################################################################################################
        #                                                                                                 #
        #                                    model validation                                             #
        #                                                                                                 #
        ###################################################################################################

        if s["run_10fold_cross_validation"]:
            thoipapy.validation.validation.run_10fold_cross_validation(s, logging)
            thoipapy.validation.validation.create_10fold_cross_validation_fig(s, logging)


        if s["run_LOO_validation"]:
            thoipapy.validation.validation.run_LOO_validation(s, df_set, logging)
            if "create_LOO_validation_figs" in s:
                if s["create_LOO_validation_figs"]:
                    thoipapy.validation.validation.create_LOO_validation_fig(s, df_set, logging)

        if s["calc_feature_importances"]:
            thoipapy.validation.validation.calc_feat_import_from_mean_decrease_impurity(s, logging)
            thoipapy.validation.validation.fig_feat_import_from_mean_decrease_impurity(s, logging)
            thoipapy.validation.validation.calc_feat_import_from_mean_decrease_accuracy(s, logging)
            thoipapy.validation.validation.fig_feat_import_from_mean_decrease_accuracy(s, logging)

        if s["train_machine_learning_model"]:
            thoipapy.validation.validation.train_machine_learning_model(s, logging)

        if s["run_testset_trainset_validation"] == True:
            thoipapy.figs.create_BOcurve_files.run_testset_trainset_validation(s, logging)

        ###################################################################################################
        #                                                                                                 #
        #                                               figures                                           #
        #                                                                                                 #
        ###################################################################################################

        Fontsize = s["Fontsize"]
        Filter = s["Filter"]
        Width= s["Width"]
        Size= s["Size"]
        Linewidth= s["Linewidth"]

        # DEPRECATED
        #if s["FigZB_07_hardlinked"] == True:
        #    # barcharts of coevolution values for interface and non-interface
        #    thoipapy.figs.other.other_figs.average_fraction_DI.FigZB_07_hardlinked(Fontsize, Width, Size, s)

        #DEPRECATED
        #if s["FigZB_18"] == True:
        #    # heatmap of prediction from THOIPA, PREDDIMER, TMDOCK
        #    thoipapy.other.other_figs.create_PREDDIMER_TMDOCK_heatmap.FigZB_18(s, Fontsize, Width, Size)

        # DEPRECATED
        #if s["combine_BOcurve_files_hardlinked"] == True:
        #    thoipapy.figs.Combine_Bo_Curve_files.combine_BOcurve_files_hardlinked(s)

        # DEPRECATED. USE COMPARE PREDICTORS
        # if s["fig_plot_BOcurve_mult_train_datasets"] == True:
        #     thoipapy.figs.Combine_Bo_Curve_files.fig_plot_BOcurve_mult_train_datasets(s)

        if s["compare_predictors"] == True:
            thoipapy.figs.combine_BOcurve_files.compare_predictors(s)

        # DEPRECATED
        #if s["run_BOcurve_comp_hardlinked"] == True:
        #    thoipapy.figs.BOcurve_THOIPAbest_comp_LIPS_and_NMR.run_BOcurve_comp_hardlinked(Fontsize, Width, Size, s, Linewidth)

        if s["calc_PREDDIMER_TMDOCK_closedist"] == True:
            thoipapy.figs.calc_PREDDIMER_TMDOCK_closedist.calc_closedist_from_PREDDIMER_TMDOCK_best_model(s, df_set, logging)

        if s["merge_predictions"] == True:
            thoipapy.validation.combine_mult_predictors.merge_predictions(s, df_set, logging)

        if s["run_indiv_validation_each_TMD"] == True:
            namedict = thoipapy.utils.create_namedict(os.path.join(s["dropbox_dir"], "protein_names.xlsx"))
            THOIPA_predictor_name = "THOIPA_{}_LOO".format(s["set_number"])
            predictor_name_list = [THOIPA_predictor_name, "PREDDIMER", "TMDOCK", "LIPS_surface_ranked"]
            #thoipapy.validation.indiv_validation.collect_indiv_validation_data(s, df_set, logging, namedict, predictor_name_list, THOIPA_predictor_name)
            thoipapy.validation.indiv_validation.create_indiv_validation_figs(s, logging, namedict, predictor_name_list, THOIPA_predictor_name)

        if s["create_merged_heatmap"] == True:
            thoipapy.figs.create_heatmap_from_merge_file.create_merged_heatmap(s, df_set, logging)

        if s["create_ROC_4predictors"] == True:
            thoipapy.validation.indiv_validation.create_ROC_comp_4predictors(s, df_set, logging)

        #if s["create_AUC_AUBOC_separate_database"] == True:
        #    thoipapy.other.validation_deprecated.validation_test_train_deprecated.create_AUBOC10_4predictors_3databases_figs(s, df_set, logging)
        #    thoipapy.other.validation_deprecated.validation_test_train_deprecated.create_AUC_4predictors_3databases_figs(s, df_set, logging)

        if "download_10_homologues_from_ncbi" in s:
            if s["download_10_homologues_from_ncbi"] == True:
                thoipapy.homologues.NCBI_download.download_10_homologues_from_ncbi(s, df_set, logging)

        if "plot_coev_vs_res_dist" in s:
            if s["plot_coev_vs_res_dist"] == True:
                thoipapy.figs.retrospective.calc_coev_vs_res_dist(s, dfset, logging)
                thoipapy.figs.retrospective.plot_coev_vs_res_dist(s, logging)

        if s["ROC_PR_val_all_residues_combined"]:
            thoipapy.validation.validation.create_ROC_all_residues(s, df_set, logging)
            thoipapy.validation.validation.create_precision_recall_all_residues(s, df_set, logging)

        thoipapy.setting.deployment_helper.docker_deployment_had_better_work_now()
        thoipapy.ML_model.deployment_helper2.docker_deployment_had_better_work_now2()

        # close the logger. A new one will be made for the next protein list.
        logging.info("FINISHED PROCESSING OF {}.".format(setname))
        logging.shutdown()
