from main import LoanCalculatorApp
from unittest.mock import patch, MagicMock
import pytest

calculator = LoanCalculatorApp()


def test_app_constructor():
    """Tests the LoanCalculatorApp class constructor"""
    calculator.window.update_idletasks()
    assert calculator.window is not None
    assert (calculator.window.winfo_width() == 550) and (calculator.window.winfo_height() == 350)
    assert calculator.window.title() == 'Loan Calculator App'
    assert calculator.window.cget('background') == '#F1D7DA'


@pytest.mark.parametrize("interest_rate, number_years, loan_amount, expected_monthly_payment", [
    (5, 1, 1000, 85.607),
    (10, 5, 5000, 106.235),
    (3, 2, 20000, 859.624)
])
def test_get_monthly_payment(interest_rate, number_years, loan_amount, expected_monthly_payment):
    """Tests the get_monthly_payment method with various input values."""
    monthly_payment = calculator.get_monthly_payment(loan_amount, interest_rate / 1200, number_years)
    assert monthly_payment == pytest.approx(expected_monthly_payment, abs=0.001)


def test_on_close_false():
    """Tests the on_close method with exit_choice == False"""
    calculator.window = MagicMock()

    with patch('main.messagebox.askyesno', return_value=False) as mock_askyesno:
        calculator.on_close()

    mock_askyesno.assert_called_once_with(title='Exit window', message='Would you like to close the program?')
    calculator.window.destroy.assert_not_called()


def test_on_close_true():
    """Tests the on_close method with exit_choice == True"""
    calculator.window = MagicMock()

    with patch('main.messagebox.askyesno', return_value=True) as mock_askyesno:
        calculator.on_close()

    mock_askyesno.assert_called_once_with(title='Exit window', message='Would you like to close the program?')
    calculator.window.destroy.assert_called_once()


@pytest.mark.parametrize("interest_rate, number_years, loan_amount, expected_monthly_payment, expected_total_payment", [
    (5, 1, 1000, 85.607, 1027.290),
    (10, 5, 5000, 106.235, 6374.113),
    (3, 2, 20000, 859.624, 20630.982),
    (12, 25, 359123, 3782.370, 1134711.041),
    (-2, 18, 50549, 194.228, 41953.250),
    (7.5, 30, 34000.569, 237.737, 85585.288)
])
def test_compute_payment_valid_input(interest_rate, number_years, loan_amount,
                                     expected_monthly_payment, expected_total_payment):
    """Tests the compute_payment method with various input values.
    Tests the correction of computing, all input values are ok."""
    calculator.entry_loan_amount.get = MagicMock(return_value=loan_amount)
    calculator.entry_interest_rate.get = MagicMock(return_value=interest_rate)
    calculator.entry_number_years.get = MagicMock(return_value=number_years)

    calculator.compute_payment()

    assert calculator.result_monthly_payment['text'] == f'{expected_monthly_payment:.3f}'
    assert calculator.result_total_payment['text'] == f'{expected_total_payment:.3f}'


@pytest.mark.parametrize("interest_rate, number_years, loan_amount", [
    (5, '1.532', 1000),
    (10, '5.0', 5000),
    ('abc', 2, 20000),
    (10, 7, 'abcd'),
    ('##287', 11.2, 'abcd'),
    ('#12', '5687h', 'abcd')
])
def test_compute_payment_invalid_input(interest_rate, number_years, loan_amount):
    """Tests, that messagebox.showerror is called when input values aren't ok."""
    calculator.entry_loan_amount.get = MagicMock(return_value=loan_amount)
    calculator.entry_interest_rate.get = MagicMock(return_value=interest_rate)
    calculator.entry_number_years.get = MagicMock(return_value=number_years)

    with patch('main.messagebox.showerror') as mock_showerror:
        calculator.compute_payment()

    mock_showerror.assert_called_once_with("Error", "Please enter valid numerical values.")

