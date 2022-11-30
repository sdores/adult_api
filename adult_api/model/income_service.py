#!/usr/bin/python3
# Copyright 2022 Sergio Doreste Buerles
# See LICENSE for details.
# Author: Sergio Doreste Buerles


import os
import keras
import numpy as np
from typing import Any, Dict, Tuple
from werkzeug.datastructures import FileStorage
from sklearn.neighbors import KNeighborsClassifier

from adult_api import logger


class AdultService:
    """Loads the model and perform predictions over it.

    Also maps results of the model
    """

    def __init__(self, model_path: str) -> None:
        """
        Args:
            model_path: the path of the pickle file where model is located
        """

        self.model = self._load_model(model_path=model_path)

    def _load_model(self
        , model_path: str
    ) -> None:
        """Loads the model into memory

        Args:
            model_path: the file system path where model is located

        Returns:
            the model path
        """

        logger.info('loading model')

        model = []
        model.append(('KNeighborsClassifier', KNeighborsClassifier(n_neighbors=20)))

        logger.info('model loaded sucessfully')

        return model

    def _map_categories(self
        , model_output: int
    ) -> str:
        """Maps the categories between the model output (int) and the desired result (str)

        Args:
            model_output: the output of the model

        Returns:
            the output
        """

        mappings = {
            0: '<=50',
            1: '>50'
        }

        if model_output not in mappings:
            logger.warning(f'trying to map model output with value of {model_output}')
            raise ValueError('The model output does not fit within the available mappings')

        mapping = mappings[model_output]

        return mapping

    def classify() -> str:
        logger.info('loading data')

        img_data = {
        'age' : '34',
        'workclass':'Private',
        'demography': '216864',
        'education':'HS-grad',
        'educaNum':'9',
        'maritalStatus':'Divorced',
        'occupation':'Other-service',
        'relationship':'Unmarried',
        'race':'White',
        'sex':'Female',
        'gainCapital':'0',
        'lossCapital':'3770',
        'hoursWork':'45',
        'country':'United-States'
        }

        logger.info('applying model')

        # apply model
        model_output = self.model.predict(img_data)

        logger.debug(f'resulting model {model_output}')
        logger.info('mapping categories')

        logger.info('prediction finished successfully')

        return result