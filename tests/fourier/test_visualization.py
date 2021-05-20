# Copyright 2018-2021 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Unit tests for :mod:`fourier` visualization functions.
"""

import pennylane as qml

import pytest

matplotlib = pytest.importorskip("matplotlib")
import matplotlib.pyplot as plt

from pennylane import numpy as np

from pennylane.fourier.visualization import _validate_coefficients

from pennylane.fourier.visualization import (
    plot_coeffs_violin,
    plot_coeffs_bar,
    plot_coeffs_box,
    plot_coeffs_panel,
    plot_coeffs_radial_box,
)


coeffs_1D_valid_1 = np.array([0.5, 0, 0.25j, 0.25j, 0])
coeffs_1D_valid_2 = [0.5, 0.1j, -0.25j, 0.25j, -0.1j]
coeffs_1D_invalid = np.array([0.5, 0, 0.25j, 0.25j])

coeffs_2D_valid_1 = np.array(
    [
        [
            0.07469786 + 0.0000e00j,
            0.0 + 4.3984e-04j,
            0.00101184 - 0.0000e00j,
            0.00101184 + 0.0000e00j,
            0.0 - 4.3984e-04j,
        ],
        [
            -0.03973803 - 1.9390e-03j,
            0.0 + 0.0000e00j,
            0.01986902 + 9.6950e-04j,
            0.01986902 + 9.6950e-04j,
            -0.0 + 0.0000e00j,
        ],
        [
            0.0121718 - 3.2000e-07j,
            0.02703674 - 7.2000e-07j,
            0.22464211 - 5.9600e-06j,
            0.22464211 - 5.9600e-06j,
            -0.02703674 + 7.2000e-07j,
        ],
        [
            0.0121718 + 3.2000e-07j,
            -0.02703674 - 7.2000e-07j,
            0.22464211 + 5.9600e-06j,
            0.22464211 + 5.9600e-06j,
            0.02703674 + 7.2000e-07j,
        ],
        [
            -0.03973803 + 1.9390e-03j,
            -0.0 - 0.0000e00j,
            0.01986902 - 9.6950e-04j,
            0.01986902 - 9.6950e-04j,
            0.0 - 0.0000e00j,
        ],
    ]
)

coeffs_2D_valid_2 = np.array(
    [
        [
            0.12707831 + 0.0j,
            -0.0 + 0.00014827j,
            0.0271287 - 0.0j,
            0.0271287 + 0.0j,
            -0.0 - 0.00014827j,
        ],
        [
            0.14675568 - 0.0061323j,
            0.0 + 0.0j,
            -0.07337784 + 0.00306615j,
            -0.07337784 + 0.00306615j,
            -0.0 - 0.0j,
        ],
        [
            0.12201549 - 0.010611j,
            0.10344825 - 0.00899631j,
            0.14288853 - 0.01242621j,
            0.14288853 - 0.01242621j,
            -0.10344825 + 0.00899631j,
        ],
        [
            0.12201549 + 0.010611j,
            -0.10344825 - 0.00899631j,
            0.14288853 + 0.01242621j,
            0.14288853 + 0.01242621j,
            0.10344825 + 0.00899631j,
        ],
        [
            0.14675568 + 0.0061323j,
            -0.0 + 0.0j,
            -0.07337784 - 0.00306615j,
            -0.07337784 - 0.00306615j,
            0.0 - 0.0j,
        ],
    ]
)

coeffs_2D_valid_list = [coeffs_2D_valid_1, coeffs_2D_valid_2]

coeffs_2D_invalid = np.array(
    [
        [
            0.12707831 + 0.0j,
            -0.0 + 0.00014827j,
            0.0271287 - 0.0j,
            0.0271287 + 0.0j,
            -0.0 - 0.00014827j,
        ],
        [
            0.14675568 - 0.0061323j,
            0.0 + 0.0j,
            -0.07337784 + 0.00306615j,
            -0.07337784 + 0.00306615j,
            -0.0 - 0.0j,
        ],
        [
            0.12201549 - 0.010611j,
            0.10344825 - 0.00899631j,
            0.14288853 - 0.01242621j,
            0.14288853 - 0.01242621j,
            -0.10344825 + 0.00899631j,
        ],
        [
            0.12201549 + 0.010611j,
            -0.10344825 - 0.00899631j,
            0.14288853 + 0.01242621j,
            0.14288853 + 0.01242621j,
            0.10344825 + 0.00899631j,
        ],
    ]
)

coeffs_3D_valid = np.array(
    [
        [
            [
                0.0 + 0.0j,
                -0.00882888 - 0.14568055j,
                0.0 - 0.0j,
                0.0 + 0.0j,
                -0.00882888 + 0.14568055j,
            ],
            [0.38262211 - 0.0j, 0.0 - 0.0j, 0.0 - 0.0j, -0.0 + 0.0j, -0.0 + 0.0j],
            [
                -0.0 - 0.03218167j,
                0.00441444 + 0.07284027j,
                -0.0 + 0.0j,
                -0.0 + 0.0j,
                0.00441444 - 0.07284027j,
            ],
            [
                -0.0 + 0.03218167j,
                0.00441444 + 0.07284027j,
                -0.0 - 0.0j,
                -0.0 - 0.0j,
                0.00441444 - 0.07284027j,
            ],
            [0.38262211 + 0.0j, -0.0 - 0.0j, -0.0 - 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        ],
        [
            [-0.0 - 0.0j, -0.0 - 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, -0.0 - 0.0j],
            [0.0 + 0.0j, -0.0 - 0.0j, -0.0 + 0.0j, 0.0 - 0.0j, 0.0 - 0.0j],
            [-0.0 + 0.0j, 0.0 + 0.0j, 0.0 - 0.0j, 0.0 + 0.0j, -0.0 - 0.0j],
            [-0.0 - 0.0j, 0.0 + 0.0j, 0.0 - 0.0j, 0.0 - 0.0j, -0.0 - 0.0j],
            [0.0 + 0.0j, 0.0 - 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        ],
        [
            [
                0.0 - 0.0j,
                0.0019699 - 0.00293059j,
                0.0 + 0.0j,
                -0.0 + 0.0j,
                -0.0023094 + 0.00267124j,
            ],
            [0.00439013 - 0.00574692j, 0.0 - 0.0j, -0.0 - 0.0j, -0.0 - 0.0j, 0.0 + 0.0j],
            [
                0.00047266 - 0.00061874j,
                -0.00098495 + 0.00146529j,
                -0.0 - 0.0j,
                -0.0 + 0.0j,
                0.0011547 - 0.00133562j,
            ],
            [
                -0.00047266 + 0.00061874j,
                -0.00098495 + 0.00146529j,
                -0.0 + 0.0j,
                -0.0 + 0.0j,
                0.0011547 - 0.00133562j,
            ],
            [0.00439013 - 0.00574692j, 0.0 - 0.0j, -0.0 + 0.0j, -0.0 + 0.0j, -0.0 + 0.0j],
        ],
        [
            [
                0.0 + 0.0j,
                -0.0023094 - 0.00267124j,
                -0.0 - 0.0j,
                0.0 - 0.0j,
                0.0019699 + 0.00293059j,
            ],
            [0.00439013 + 0.00574692j, -0.0 - 0.0j, -0.0 - 0.0j, -0.0 - 0.0j, 0.0 + 0.0j],
            [
                -0.00047266 - 0.00061874j,
                0.0011547 + 0.00133562j,
                -0.0 - 0.0j,
                -0.0 - 0.0j,
                -0.00098495 - 0.00146529j,
            ],
            [
                0.00047266 + 0.00061874j,
                0.0011547 + 0.00133562j,
                -0.0 - 0.0j,
                -0.0 + 0.0j,
                -0.00098495 - 0.00146529j,
            ],
            [0.00439013 + 0.00574692j, 0.0 - 0.0j, -0.0 + 0.0j, -0.0 + 0.0j, 0.0 + 0.0j],
        ],
        [
            [-0.0 + 0.0j, -0.0 + 0.0j, 0.0 - 0.0j, 0.0 - 0.0j, -0.0 + 0.0j],
            [0.0 - 0.0j, 0.0 - 0.0j, 0.0 - 0.0j, 0.0 - 0.0j, 0.0 + 0.0j],
            [-0.0 + 0.0j, -0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 - 0.0j],
            [-0.0 - 0.0j, -0.0 + 0.0j, 0.0 - 0.0j, 0.0 + 0.0j, 0.0 - 0.0j],
            [0.0 - 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, -0.0 - 0.0j, -0.0 + 0.0j],
        ],
    ]
)

fig_valid, ax_valid = plt.subplots(2, 1, sharex=True, sharey=True)
fig_invalid, ax_invalid = plt.subplots(3, 1, sharex=True, sharey=True)
fig_panel_invalid, ax_panel_invalid = plt.subplots(3, 2, sharex=True, sharey=True)


class TestValidateCoefficients:
    """Test Fourier coefficients are properly validated/invalidated."""

    @pytest.mark.parametrize(
        "coeffs,n_inputs,can_be_list,expected_coeffs",
        [
            (coeffs_1D_valid_1, 1, True, np.array([coeffs_1D_valid_1])),
            (coeffs_1D_valid_1, 1, False, np.array(coeffs_1D_valid_1)),
            (coeffs_1D_valid_2, 1, True, np.array([coeffs_1D_valid_2])),
            (coeffs_1D_valid_2, 1, False, coeffs_1D_valid_2),
            (coeffs_2D_valid_1, 2, True, np.array([coeffs_2D_valid_1])),
            (coeffs_2D_valid_list, 2, True, np.array(coeffs_2D_valid_list)),
            (coeffs_3D_valid, 3, True, np.array([coeffs_3D_valid])),
            (coeffs_3D_valid, 3, False, coeffs_3D_valid),
        ],
    )
    def test_valid_fourier_coeffs(self, coeffs, n_inputs, can_be_list, expected_coeffs):
        """Check that valid parameters are properly processed."""
        obtained_coeffs = _validate_coefficients(coeffs, n_inputs, can_be_list)
        assert np.allclose(obtained_coeffs, expected_coeffs)

    def test_incorrect_type_fourier_coeffs(self):
        """Check that invalid type of parameters is caught"""
        with pytest.raises(TypeError, match="must be a list of numerical"):
            _validate_coefficients("A", True)

    @pytest.mark.parametrize(
        "coeffs,n_inputs,can_be_list,expected_error_message",
        [
            (coeffs_1D_invalid, 1, True, "Shape of input coefficients must be 2d"),
            (coeffs_1D_valid_1, 2, True, "Plotting function expected a list of"),
            (coeffs_2D_invalid, 2, False, "All dimensions of coefficient array must be the same"),
        ],
    )
    def test_invalid_fourier_coeffs(self, coeffs, n_inputs, can_be_list, expected_error_message):
        """Check invalid Fourier coefficient inputs are caught."""
        with pytest.raises(ValueError, match=expected_error_message):
            _validate_coefficients(coeffs, n_inputs, can_be_list)


class TestInvalidAxesPassing:
    """Test that axes of the incorrect type are not plotted on."""

    @pytest.mark.parametrize(
        "func,coeffs,n_inputs,ax,expected_error_message",
        [
            (
                plot_coeffs_violin,
                coeffs_1D_valid_1,
                1,
                ax_invalid,
                "Matplotlib axis should consist of two subplots.",
            ),
            (
                plot_coeffs_box,
                coeffs_1D_valid_2,
                1,
                ax_invalid,
                "Matplotlib axis should consist of two subplots.",
            ),
            (
                plot_coeffs_bar,
                coeffs_1D_valid_1,
                1,
                ax_invalid,
                "Matplotlib axis should consist of two subplots.",
            ),
            (
                plot_coeffs_radial_box,
                coeffs_2D_valid_list,
                2,
                ax_invalid,
                "Matplotlib axis should consist of two subplots.",
            ),
            (
                plot_coeffs_panel,
                coeffs_2D_valid_list,
                2,
                ax_panel_invalid,
                "Shape of subplot axes must match the shape of the coefficient data.",
            ),
        ],
    )
    def test_invalid_axes(self, func, coeffs, n_inputs, ax, expected_error_message):
        """Test that invalid axes are not plotted on."""
        with pytest.raises(ValueError, match=expected_error_message):
            func(coeffs, n_inputs, ax)
