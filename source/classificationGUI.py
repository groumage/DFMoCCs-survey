"""!
@file classificationGUI.py
@author guillaume.roumage.research@proton.me
@date 21604/2025

@brief This file contains the GUI for the dataflow models classification.
"""

##
# @mainpage
# 
# @section description Description
#
# This program is a GUI for the expressiveness and analyzability hierarchy presented in the survey of dataflow models [1] and its extended version [2]. It allows system designers to visualize the expressiveness and analyzability score based on an interactive choice of weighted features and static analyses. A 2D graph is also displayed to visualize the expressiveness and analyzability scores of the selected dataflow models.
#
# @section usage Usage
#
# @subsection run_gui Running the GUI
#
# The GUI can be run using docker:
# ```bash
# docker build -t dfmoccsgui . && docker run -it --rm -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY dfmoccsgui
# ```
# where `<path_to_hierarchy_file>` is the path to the JSON file containing the hierarchy. If no path is provided, the program will use the default hierarchy file `resources/hierarchy-example.json`.
#
# If you manage to have all python dependencies installed, you can run the GUI without docker:
# ```bash
# python3 source/classificationGUI.py
# ```
# @subsection des_gui GUI description
#
# \image html gui-description.png width=50%
#
# Below is the description of elements labeled as defined in the figure above:
#
# 1. This table displays all dataflow models which:
#   - have either all or at least one feature selected in the list labeled as 2 (cf. item 2),
#   - have either all or at least one static analyses selected in the list labeled as 3 (cf. item 3),
#   - and belong to a category selected in the checkboxes area labeled as 4 (cf. item 4).
# 2. This list contains all features used to classify the dataflow models. If the *All* radio button is selected, the dataflow model must have all the selected features to be displayed in the table. If the *Any* radio button is selected, the dataflow model must have at least one of the selected features to be displayed in the table.
# 3. This list contains all static analyses used to classify the dataflow models. If the *All* radio button is selected, the dataflow model must have all the selected static analyses to be displayed in the table. If the *Any* radio button is selected, the dataflow model must have at least one of the selected static analyses to be displayed in the table.
# 4. This area contains the checkboxes to select the categories of dataflow models to be displayed in the table.
# 5. This graph displays the expressiveness and analyzability scores of the selected dataflow models under a 2D graph. The x-axis represents the expressiveness score and the y-axis represents the analyzability score. A selection of a dataflow model in the table will highlight the corresponding point in the graph and will update its description (cf. item 7).
# 6. This area allow to change the coefficient assigned to categories 1 and 2 and to move features and static analyses from one category to another.
# 7. This area displays the description of the selected dataflow models in the table.
# 8. Those buttons allow to import a hierarchy JSON file and to export the current displayed hierarchy to a JSON file.
#
# @section dev_guide Developer Guide
#
# This program is intended to be extended by systems designers, researchers, and engineers who want to add new features, static analyses, or dataflow models. Hereafter are some guidelines to help you get started.
#
# 1. **Adding a new feature**: To add new features, modify the `resources/features.json` file. All features are listed in a json file where key is the abbreviation of the feature and value is the name of the feature.
#
# 2. **Adding a new static analysis**: To add new static analyses, modify the `resources/analyzability.json` file. All static analyses are listed in a json file where key is the abbreviation of the static analysis and value is the name of the static analysis.
#
# 3. **Adding a new dataflow model**: To add new dataflow models, modify the `resources/classification.json` file. All dataflow models are listed in a json file where each entry has the following structure:
# ```json
# {
#     "dataflow_model_name": {
#         "name": String,
#         "description": String,
#         "category": String,
#         "rate_updates": list of String (of at least one element),
#         "topology_updates": list of String (of at least one element),
#         "range_rate": String,
#         "features": list of String (possibly empty),
#         "analyzability": list of String (possibly empty),
#         "turing_complete": Boolean
# }
#```
#   where:
#   - `name` is a string representing the abbreviation of the dataflow model,
#   - `description` is a string representing the full name of the dataflow model,
#   - `category` is a string representing the category of the dataflow model. The category is one of the following values:
#     - *Synchronous dataflow and related DF MoCCs*,
#     - *Phased-based DF MoCCs*,
#     - *Time-based DF MoCCs*,
#     - *Boolean-based DF MoCCs*,
#     - *Scenario-based DF MoCCs*,
#     - *Meta-models DF MoCCs*,
#     - *DF MoCCs with enable and invoke capabilities*,
#     - *Process-network based DF MoCCs*,
#   - `rate_updates` is a set containing at least one of the following values: *never*, *biso*, *biro*, *wiso*, *wiro*. The content of this set depends on rate update policy of the dataflow model,
#   - `topology_updates` is a set containing at least one of the following values: *never*, *biso*, *biro*, *wiso*, *wiro*. The content of this set depends on topology update policy of the dataflow model,
#   - `range_rate` is a string representing the rate range of the dataflow model. The possible values are: {1}, *N\**, *N*, *Q\**, *Omega*,
#   - `features` is a set containing the features of the dataflow model. The content of the set is the features depends on dataflow model's rules,
#   - `analyzability` is a set containing the static analyses of the dataflow model. The content of the set is the static analyses depends on dataflow model's rules,
#   - `turing_complete` is a boolean value indicating whether the dataflow model is Turing complete or not. The possible values are: *true*, *false*, *null*. The value *null* is used for meta-models dataflow models, for which the Turing completeness is not defined.
#
# @note While a new dataflow model added in the `resources/classification.json` file is immediately available in the GUI, the new features and static analyses added in the `resources/features.json` and `resources/analyzability.json` files are not. To make them available in the GUI, checkboxes must be added in the GUI. Unfortunately, I didn't find a way to do it automatically. So, you have to add them manually in the QT Designer. To do so, open the `main_window.ui` file in the QT Designer and add as much as checkboxes as you want. The text of the checkbox **must be the same** as the name of the feature or static analysis in the `resources/features.json` and `resources/analyzability.json` files, e.g., the text of the checkbox related to the feature `"bf": "Blocking factor"` in the `resources/features.json` file is `Blocking factor` (case sensitive).
#
# The following command line generates the main_window_ui.py file from the main_window.ui file:
# ```bash
# pyuic5 -o source/main_window_ui.py resources/main_window.ui
# ```
#
# @section references References
#
# [1] G. Roumage, S. Azaiez and S. Louise, "A survey of main dataflow MoCCs for CPS design and verification", 2022 IEEE 15th International Symposium on Embedded Multicore/Many-core Systems-on-Chip (MCSoC), Penang, Malaysia, 2022, pp. 1-9, doi: 10.1109/MCSoC57363.2022.00010.
#
# [2] G. Roumage, S. Azaiez, C. Faure and S. Louise, "An Extended Survey and a Comparison Framework for Dataflow Models of Computation and Communication", arXiv, 2025, https://arxiv.org/abs/2501.07273.

import sys
import json
import argparse

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.QtWidgets import QCheckBox, QTableWidgetItem, QRadioButton, QDialog, QVBoxLayout, QLabel, QFileDialog
from main_window_ui import Ui_MainWindow

class classificationGUI(QMainWindow, Ui_MainWindow):
    """!
    @brief This class implements the GUI for the dataflow models classification.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.initialGuiConfiguration()
        self.loadData()
        self.loadHierarchy('resources/hierarchy-example.json')
        self.updateTable()
        
    def initialGuiConfiguration(self):
        """!
        @brief Initialize the GUI configuration.
        """
        self.category_1_list.clear()
        self.category_2_list.clear()
        self.features = {}
        self.analyzability = {}
        self.dataflow_models = {}
        for child in self.features_frame.findChildren(QCheckBox):
            child.setChecked(True)
        for child in self.analyzability_frame.findChildren(QCheckBox):
            child.setChecked(True)
        self.show_non_turing_complete_check_box.setChecked(True)
        self.show_turing_complete_check_box.setChecked(True)
        self.show_meta_models_check_box.setChecked(True)
        self.any_radio_button_features.setChecked(True)
        self.any_radio_button_analyzability.setChecked(True)
        self.graph.clear()
        self.graph.getAxis('left').setPen('k')
        self.graph.getAxis('bottom').setPen('k')
        self.graph.setBackground('w')
        self.graph.setLabel('left', 'Analyzability')
        self.graph.setLabel('bottom', 'Expressiveness')
        self.rate_updates_content_label.setText('N/A')
        self.topology_updates_content_label.setText('N/A')
        self.domain_rate_content_label.setText('N/A')
        self.features_content_label.setText('N/A')
        self.analyzability_content_label.setText('N/A')
        self.table.setRowCount(0)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Model', 'Expressiveness', 'Analyzability'])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.actionAbout.triggered.connect(self.showAbout)
        self.importHierarchyButton.clicked.connect(self.selectNewHierarchyJSONFile)
        self.exportHierarchyButton.clicked.connect(self.exportHierarchyJSONFile)
    
    def loadData(self):
        """!
        @brief Load features, static analyses and the classification from JSON files.
        """
        with open('resources/features.json') as f:
            self.features = json.load(f)
        for value in self.features.values():
            self.category_1_list.addItem(value)
        self.category_1_list.addItem('Domain rate')
        self.category_1_list.addItem('Rate and topology dynamism')
        with open('resources/analyzability.json') as f:
            self.analyzability = json.load(f)
        for value in self.analyzability.values():
            self.category_1_list.addItem(value)
        with open('resources/classification.json') as f:
            self.dataflow_models = json.load(f)
    
    def selectNewHierarchyJSONFile(self):
        """!
        @brief Open a file dialog to select a new JSON hierarchy file.
        """
        hierarchy, _ = QFileDialog.getOpenFileName(self, "Open Hierarchy File", "", "JSON Files (*.json)")
        if hierarchy:
            self.loadHierarchy(hierarchy)
            
    
    def loadHierarchy(self, hierarchy):
        """!
        @brief Load the hierarchy from a JSON file.
        """
        with open(hierarchy) as f:
            hierarchy = json.load(f)
            if 'category_1' in hierarchy and 'category_2' in hierarchy:
                self.coefficient_category_1_spin_box.setValue(hierarchy['category_1']['coefficient'])
                self.coefficient_category_2_spin_box.setValue(hierarchy['category_2']['coefficient'])
                self.category_1_list.clear()
                self.category_2_list.clear()
                for value in hierarchy['category_1']['features']:
                    self.category_1_list.addItem(value)
                for value in hierarchy['category_2']['features']:
                    self.category_2_list.addItem(value)
            else:
                self.error_dialog = QDialog(self)
                self.error_dialog.setWindowTitle("Error")
                self.error_dialog.setModal(True)
                self.error_dialog.setFixedSize(300, 100)
                layout = QVBoxLayout()
                label = QLabel()
                label.setWordWrap(True)
                label.setText("The JSON file is not valid. Please check the format.")
                label.setTextInteractionFlags(Qt.TextSelectableByMouse)
                layout.addWidget(label)
                self.error_dialog.setLayout(layout)
                self.error_dialog.exec_()
    
    def exportHierarchyJSONFile(self):
        """!
        @brief Open a file dialog to export the hierarchy to a JSON file.
        """
        hierarchy, _ = QFileDialog.getSaveFileName(self, "Save Hierarchy File", "", "JSON Files (*.json)")
        if hierarchy:
            hierarchy_data = {
                'category_1': {
                    'coefficient': self.coefficient_category_1_spin_box.value(),
                    'features': [self.category_1_list.item(i).text() for i in range(self.category_1_list.count())]
                },
                'category_2': {
                    'coefficient': self.coefficient_category_2_spin_box.value(),
                    'features': [self.category_2_list.item(i).text() for i in range(self.category_2_list.count())]
                }
            }
            with open(hierarchy, 'w') as f:
                json.dump(hierarchy_data, f, indent=4)
    
    def showAbout(self):
        """!
        @brief Show the about dialog.
        """
        self.about_dialog = QDialog(self)
        self.about_dialog.setWindowTitle("About")
        self.about_dialog.setModal(True)
        self.about_dialog.setFixedSize(550, 300)
        layout = QVBoxLayout()
        label = QLabel()
        label.setWordWrap(True)
        label.setText(
            "This program is a GUI for the survey of dataflow models [1] and its extended version [2].\n"
            "Version 1.0\n"
            "Author: Guillaume Roumage (guillaume.roumage.research@proton.me)\n"
            "Last update: 21/04/2025\n\n"
            "[1] G. Roumage, S. Azaiez and S. Louise, \"A survey of main dataflow MoCCs for CPS design and verification\", 2022 IEEE 15th International Symposium on Embedded Multicore/Many-core Systems-on-Chip (MCSoC), Penang, Malaysia, 2022, pp. 1-9, doi: 10.1109/MCSoC57363.2022.00010.\n"
            "[2] G. Roumage, S. Azaiez, C. Faure and S. Louise, \"An Extended Survey and a Comparison Framework for Dataflow Models of Computation and Communication\", arXiv, 2025, https://arxiv.org/abs/2501.07273."
        )
        label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        layout.addWidget(label)
        self.about_dialog.setLayout(layout)
        self.about_dialog.exec_()
    
    def connectSignalsSlots(self):
        """!
        @brief Connect the signals and slots of the GUI.
        """
        self.show_non_turing_complete_check_box.clicked.connect(self.updateTable)
        self.show_turing_complete_check_box.clicked.connect(self.updateTable)
        self.show_meta_models_check_box.clicked.connect(self.updateTable)
        self.coefficient_category_1_spin_box.valueChanged.connect(self.updateTable)
        self.coefficient_category_2_spin_box.valueChanged.connect(self.updateTable)
        self.table.clicked.connect(self.updateGraph)
        self.table.clicked.connect(self.updateDescription)
        self.right_button.clicked.connect(self.moveRight)
        self.left_button.clicked.connect(self.moveLeft)
        for child in self.features_frame.findChildren(QCheckBox):
            child.clicked.connect(self.updateTable)
        for child in self.group_radio_button_features.findChildren(QRadioButton):
            child.clicked.connect(self.updateTable)
        for child in self.analyzability_frame.findChildren(QCheckBox):
            child.clicked.connect(self.updateTable)
        for child in self.group_radio_button_analyzability.findChildren(QRadioButton):
            child.clicked.connect(self.updateTable)
    
    def getModelsToPrint(self):
        """Get the dataflow models to print based on the selected checkboxes and radio buttons."""
        modelsToPrint = []
        if self.show_non_turing_complete_check_box.isChecked():
            nonTuringModels = self.getNonTuringModels
            for model in nonTuringModels:
                if self.hasSelectedFeatures(model) and self.hasCheckedAnalyzability(model):
                    modelsToPrint.append(model)
        if self.show_turing_complete_check_box.isChecked():
            turingCompleteModels = self.getTuringModels
            for model in turingCompleteModels:
                if self.hasSelectedFeatures(model) and self.hasCheckedAnalyzability(model):
                    modelsToPrint.append(model)
        if self.show_meta_models_check_box.isChecked():
            metaModels = self.getMetaModels
            for model in metaModels:
                if self.hasSelectedFeatures(model) and self.hasCheckedAnalyzability(model):
                    modelsToPrint.append(model)
        return list(set(modelsToPrint))

    def hasSelectedFeatures(self, model):
        """!
        @brief Check if the model has all the selected features if the 'All' radio button is checked, or if it has at least one selected features if the 'Any' radio button is checked.
        @param model The model to check. 
        @return True if the model has the selected features, False otherwise.
        """
        if self.isAllFeatureRadioButtonChecked():
            for child in self.features_frame.findChildren(QCheckBox):
                if child.isChecked() and not model in [k for k, v in self.dataflow_models.items() if self.getFeatureAbreviation(child.text()) in v['features']]:
                    return False
            return True
        else:
            for child in self.features_frame.findChildren(QCheckBox):
                if child.isChecked() and model in [k for k, v in self.dataflow_models.items() if self.getFeatureAbreviation(child.text()) in v['features']]:
                    return True
            return False

    def hasCheckedAnalyzability(self, model):
        """!
        @brief Check if the model has all the selected static analyses if the 'All' radio button is checked, or if it has at least one selected static analysis if the 'Any' radio button is checked.
        @param model The model to check.
        @return True if the model has the selected static analyses, False otherwise.
        """
        if self.isAllAnalyzabilityRadioButtonChecked():
            for child in self.analyzability_frame.findChildren(QCheckBox):
                if child.isChecked() and not model in [k for k, v in self.dataflow_models.items() if self.getAnalyzabilityAbreviation(child.text()) in v['analyzability']]:
                    return False
            return True
        else:
            for child in self.analyzability_frame.findChildren(QCheckBox):
                if child.isChecked() and model in [k for k, v in self.dataflow_models.items() if self.getAnalyzabilityAbreviation(child.text()) in v['analyzability']]:
                    return True
            return False

    def isAllFeatureRadioButtonChecked(self):
        """!
        @brief Check if the 'All' radio button of features is checked for features.
        @return True if the 'All' radio button of features is checked, False otherwise.
        """
        return self.all_radio_button_features.isChecked()
    
    def isAllAnalyzabilityRadioButtonChecked(self):
        """!
        @brief Check if the 'All' radio button of static analyses is checked for analyzability.
        @return True if the 'All' radio button of static analyses is checked, False otherwise.
        """
        return self.all_radio_button_analyzability.isChecked()
    
    def getFeatureAbreviation(self, feature):
        """Get the abbreviation of the feature."""
        return next((k for k, v in self.features.items() if v == feature), None)

    def getAnalyzabilityAbreviation(self, analyzability):
        """Get the abbreviation of the static analysis."""
        return next((k for k, v in self.analyzability.items() if v == analyzability), None)

    def getExpressivenessScore(self, models):
        """!
        @brief Get the expressiveness score of the printed models based on the selected features and static analyses.
        @param models The models for which the expressiveness score is calculated.
        @return A list of expressiveness scores for the printed models.
        """
        expressiveness_score = []
        for model in models:
            expressiveness = 0
            for k, v in self.features.items():
                if k in self.dataflow_models[model]['features']:
                    expressiveness += self.coefficient_category_1_spin_box.value() if v in [self.category_1_list.item(i).text() for i in range(self.category_1_list.count())] else self.coefficient_category_2_spin_box.value()
            expressiveness += (self.getRateRangeScore(self.dataflow_models[model]['range_rate']) * self.coefficient_category_1_spin_box.value()) if 'Domain rate' in [self.category_1_list.item(i).text() for i in range(self.category_1_list.count())] else self.coefficient_category_2_spin_box.value()
            expressiveness += (self.getRateTopologyUpdatesScore(self.dataflow_models[model]['rate_updates'], self.dataflow_models[model]['topology_updates']) * self.coefficient_category_1_spin_box.value()) if 'Rate and topology dynamism' in [self.category_1_list.item(i).text() for i in range(self.category_1_list.count())] else self.coefficient_category_2_spin_box.value()
            expressiveness_score.append(expressiveness)
        return expressiveness_score

    def getRateRangeScore(self, range_rate):
        """!
        @brief Get the score of the rate range.
        @param range_rate The rate range to check.
        @return The score of the rate range.
        """
        score = 0
        if range_rate == '{1}':
            score += 0
        elif range_rate == 'N*':
            score += 1
        elif range_rate == 'N':
            score += 2
        elif range_rate == 'Q*':
            score += 3
        elif range_rate == 'Omega':
            score += 4
        return score / 4
    
    def getRateTopologyUpdatesScore(self, rate_updates, topology_updates):
        """!
        @brief Get the score of the rate and topology updates.
        @param rate_updates The rate updates to check.
        @param topology_updates The topology updates to check.
        @return The score of the rate and topology updates.
        """
        score = 0
        if len(rate_updates) == 1:
            if rate_updates[0] == 'never':
                score += 0
            elif rate_updates[0] == 'biso':
                score += 2
            elif rate_updates[0] == 'biro':
                score += 4
            elif rate_updates[0] == 'wiso':
                score += 6
            elif rate_updates[0] == 'wiro':
                score += 8
        elif len(rate_updates) == 2:
            if (rate_updates[0] == 'never' and rate_updates[1] == 'biso') or (rate_updates[0] == 'biso' and rate_updates[1] == 'never'):
                score += 1
            elif (rate_updates[0] == 'never' and rate_updates[1] == 'biro') or (rate_updates[0] == 'biro' and rate_updates[1] == 'never'):
                score += 2
            elif (rate_updates[0] == 'never' and rate_updates[1] == 'wiso') or (rate_updates[0] == 'biso' and rate_updates[1] == 'biro') or (rate_updates[0] == 'biro' and rate_updates[1] == 'biso') or (rate_updates[0] == 'wiso' and rate_updates[1] == 'never'):
                score += 3
            elif (rate_updates[0] == 'never' and rate_updates[1] == 'wiro') or (rate_updates[0] == 'biso' and rate_updates[1] == 'wiso') or (rate_updates[0] == 'wiso' and rate_updates[1] == 'biso') or (rate_updates[0] == 'wiro' and rate_updates[1] == 'never'):
                score += 4
            elif (rate_updates[0] == 'biso' and rate_updates[1] == 'wiro') or (rate_updates[0] == 'biro' and rate_updates[1] == 'wiso') or (rate_updates[0] == 'wiso' and rate_updates[1] == 'biro') or (rate_updates[0] == 'wiro' and rate_updates[1] == 'biso'):
                score += 5
            elif (rate_updates[0] == 'biro' and rate_updates[1] == 'wiro') or (rate_updates[0] == 'wiro' and rate_updates[1] == 'biro'):
                score += 6
            elif (rate_updates[0] == 'wiso' and rate_updates[1] == 'wiro') or (rate_updates[0] == 'wiro' and rate_updates[1] == 'wiso'):
                score += 7
        if len(topology_updates) == 1:
            if topology_updates[0] == 'never':
                score += 0
            elif topology_updates[0] == 'biso':
                score += 2
            elif topology_updates[0] == 'biro':
                score += 4
            elif topology_updates[0] == 'wiso':
                score += 6
            elif topology_updates[0] == 'wiro':
                score += 8
        elif len(topology_updates) == 2:
            if (topology_updates[0] == 'never' and topology_updates[1] == 'biso') or (topology_updates[0] == 'biso' and topology_updates[1] == 'never'):
                score += 1
            elif (topology_updates[0] == 'never' and topology_updates[1] == 'biro') or (topology_updates[0] == 'biro' and topology_updates[1] == 'never'):
                score += 2
            elif (topology_updates[0] == 'never' and topology_updates[1] == 'wiso') or (topology_updates[0] == 'biso' and topology_updates[1] == 'biro') or (topology_updates[0] == 'biro' and topology_updates[1] == 'biso') or (topology_updates[0] == 'wiso' and topology_updates[1] == 'never'):
                score += 3
            elif (topology_updates[0] == 'never' and topology_updates[1] == 'wiro') or (topology_updates[0] == 'biso' and topology_updates[1] == 'wiso') or (topology_updates[0] == 'wiso' and topology_updates[1] == 'biso') or (topology_updates[0] == 'wiro' and topology_updates[1] == 'never'):
                score += 4
            elif (topology_updates[0] == 'biso' and topology_updates[1] == 'wiro') or (topology_updates[0] == 'biro' and topology_updates[1] == 'wiso') or (topology_updates[0] == 'wiso' and topology_updates[1] == 'biro') or (topology_updates[0] == 'wiro' and topology_updates[1] == 'biso'):
                score += 5
            elif (topology_updates[0] == 'biro' and topology_updates[1] == 'wiro') or (topology_updates[0] == 'wiro' and topology_updates[1] == 'biro'):
                score += 6
            elif (topology_updates[0] == 'wiso' and topology_updates[1] == 'wiro') or (topology_updates[0] == 'wiro' and topology_updates[1] == 'wiso'):
                score += 7
        return score / 8
    
    def getAnalyzability(self, models):
        """!
        @brief Get the analyzability score of the printed models based on the selected static analyses.
        @param models The for which the analyzability score is calculated.
        @return A list of analyzability scores for the printed models.
        """
        analyzability_score = []
        for model in models:
            analyzability = 0
            for k, v in self.analyzability.items():
                if k in self.dataflow_models[model]['analyzability']:
                    analyzability += self.coefficient_category_1_spin_box.value() if v in [self.category_1_list.item(i).text() for i in range(self.category_1_list.count())] else self.coefficient_category_2_spin_box.value()
            analyzability_score.append(analyzability)
        return analyzability_score

    def updateTable(self):
        """!
        @brief Update the summary list and the graph with the selected dataflow models.
        """
        models = self.getModelsToPrint()
        expressiveness = self.getExpressivenessScore(models)
        analyzability = self.getAnalyzability(models)
        self.fillTable(models, expressiveness, analyzability)
        self.updateGraph()
    
    def updateGraph(self):
        """!
        @brief Update the graph with the selected dataflow models and highlight the selected model.
        """
        models = self.getModelsToPrint()
        expressiveness = self.getExpressivenessScore(models)
        analyzability = self.getAnalyzability(models)
        modelsWithExpressivenessAndAnalyzability = {}
        for m, e, a in zip(models, expressiveness, analyzability):
            modelsWithExpressivenessAndAnalyzability[m] = {'expressiveness': e, 'analyzability': a}
        selected_row = self.table.currentRow()
        if selected_row == -1:
            self.fillGraph(modelsWithExpressivenessAndAnalyzability)
        else:
            selected_model = self.table.item(selected_row, 0).text()
            highlight = next((k for k, v in self.dataflow_models.items() if v['name'] == selected_model), None)
            self.fillGraph(modelsWithExpressivenessAndAnalyzability, highlight=highlight)
    
    def updateDescription(self):
        """!
        @brief Update the description of the selected model in the table (features, static analyses, rate updates, topology updates, domain rate).
        """
        selected_row = self.table.currentRow()
        if selected_row == -1:
            self.rate_updates_content_label.setText('N/A')
            self.topology_updates_content_label.setText('N/A')
            self.domain_rate_content_label.setText('N/A')
            self.features_content_label.setText('N/A')
            self.analyzability_content_label.setText('N/A')
        else:
            selected_model = self.table.item(selected_row, 0).text()
            model = next((k for k, v in self.dataflow_models.items() if v['name'] == selected_model), None)
            self.rate_updates_content_label.setText(', '.join(self.dataflow_models[model]['rate_updates']))
            self.topology_updates_content_label.setText(', '.join(self.dataflow_models[model]['topology_updates']))
            self.domain_rate_content_label.setText(self.dataflow_models[model]['range_rate'])
            self.features_content_label.setText(', '.join(self.dataflow_models[model]['features']))
            self.analyzability_content_label.setText(', '.join(self.dataflow_models[model]['analyzability']))

    def fillTable(self, models, expressiveness, analyzability):
        """!
        @brief Fill the table with the selected dataflow models.
        @param models The models to fill the table with.
        @param expressiveness The expressiveness scores of the models.
        @param analyzability The analyzability scores of the models.
        """
        self.table.setRowCount(len(models))
        self.table.setSortingEnabled(False) # https://stackoverflow.com/questions/7960505/strange-qtablewidget-behavior-not-all-cells-populated-after-sorting-followed-b
        for i, model in enumerate(models):
            self.table.setItem(i, 0, QTableWidgetItem(str(self.dataflow_models[model]['name'])))
            if expressiveness[i] < 10:
                self.table.setItem(i, 1, QTableWidgetItem("0" + str(expressiveness[i])))
            else:
                self.table.setItem(i, 1, QTableWidgetItem(str(expressiveness[i])))
            if analyzability[i] < 10:
                self.table.setItem(i, 2, QTableWidgetItem("0" + str(analyzability[i])))
            else:
                self.table.setItem(i, 2, QTableWidgetItem(str(analyzability[i])))
        self.table.setSortingEnabled(True)
    
    def fillGraph(self, data, highlight=None):
        """!
        @brief Fill the graph with the selected dataflow models.
        @param data The data to fill the graph with which contains the expressiveness and analyzability scores of the models.
        @param highlight The model to highlight in the graph.
        """
        self.graph.clear()
        expressiveness = [v['expressiveness'] for v in data.values()]
        analyzability = [v['analyzability'] for v in data.values()]
        self.graph.plot(expressiveness, analyzability, pen=None, symbol='+', symbolPen=None, symbolBrush='black')
        if highlight:
            self.graph.plot([data[highlight]['expressiveness']], [data[highlight]['analyzability']], pen=None, symbol='o', symbolPen=None, symbolBrush='red')
    
    def moveRight(self):
        """!
        @brief Move the selected item from category 1 to category 2.
        """
        self.category_2_list.addItems([str(item.text()) for item in self.category_1_list.selectedItems()])
        self.category_1_list.takeItem(self.category_1_list.currentRow())
        self.updateTable()
    
    def moveLeft(self):
        """!
        @brief Move the selected item from category 2 to category 1.
        """
        self.category_1_list.addItems([str(item.text()) for item in self.category_2_list.selectedItems()])
        self.category_2_list.takeItem(self.category_2_list.currentRow())
        self.updateTable()

    @property
    def getMetaModels(self):
        """Get the meta models."""
        return [k for k, v in self.dataflow_models.items() if v['turing_complete'] == None]
    
    @property
    def getTuringModels(self):
        """Get the Turing complete models."""
        return [k for k, v in self.dataflow_models.items() if v['turing_complete'] == True]
    
    @property
    def getNonTuringModels(self):
        """Get the non-Turing complete models."""
        return [k for k, v in self.dataflow_models.items() if (v['turing_complete'] == False)]

class MyApp(QApplication):

    def __init__(self, *args):
        super().__init__(*args)
        self.window = classificationGUI()
        self.show()
    
    def show(self):
        self.window.show()

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Dataflow models classification')
    parser.add_argument('--hierarchy', type=str, default='resources/hierarchy-example.json', help='Initialize the visualization with an existing classification')
    args = parser.parse_args()
    myapp = MyApp([args.hierarchy])
    sys.exit(myapp.exec())