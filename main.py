""" import of elements from tkinter."""
from tkinter import Tk, Label, Entry, Button, messagebox


class LoanCalculatorApp:
    """This class represents an app for loan computing.
    It creates GUI by using tkinter library for input data
    about annual interest rate, number of years and loan amount."""
    def __init__(self) -> None:
        self.window: Tk = Tk()
        self.window.geometry('550x350')
        self.window.title('Loan Calculator App')
        self.window.configure(background='#F1D7DA')

        Label(self.window, background='#F1D7DA', text='Annual Interest Rate: ',
              font=("Helvetica", 13)).grid(
              column=0, row=0, padx=10, pady=10, sticky='w')

        self.entry_interest_rate: Entry = Entry(self.window)
        self.entry_interest_rate.grid(column=1, row=0)

        Label(self.window, background='#F1D7DA', text='Number Of Years: ',
              font=("Helvetica", 13)).grid(
              column=0, row=1, padx=10, pady=10, sticky='w')

        self.entry_number_years: Entry = Entry(self.window)
        self.entry_number_years.grid(column=1, row=1)

        Label(self.window, background='#F1D7DA', text='Loan amount: ',
              font=("Helvetica", 13)).grid(
              column=0, row=2, padx=10, pady=10, sticky='w')

        self.entry_loan_amount: Entry = Entry(self.window)
        self.entry_loan_amount.grid(column=1, row=2)

        Label(self.window, background='#F1D7DA', text='Monthly Payment: ',
              font=("Helvetica", 13)).grid(
              column=0, row=3, padx=10, pady=10, sticky='w')

        Label(self.window, background='#F1D7DA', text='Total Payment: ',
              font=("Helvetica", 13)).grid(
              column=0, row=4, padx=10, pady=10, sticky='w')

        Button(self.window, text='Compute Payment',
               command=self.compute_payment, font=("Helvetica", 12),
               bg="#4CAF50", fg="white").grid(column=1, row=5)

        self.result_monthly_payment: Label = Label(self.window, background='#F1D7DA',
                                            text='', font=("Helvetica", 14))
        self.result_monthly_payment.grid(column=1, row=3,
                                         padx=10, pady=10)

        self.result_total_payment: Label = Label(self.window, background='#F1D7DA',
                                          text='', font=("Helvetica", 14))
        self.result_total_payment.grid(column=1, row=4,
                                       padx=10, pady=10)

        self.window.protocol("WM_DELETE_WINDOW",  self.on_close)
        # self.window.mainloop()

    def get_monthly_payment(self, loan_amount: float,
                            monthly_interest_rate: float, number_of_years: int) -> float:
        """Method for monthly payment calculation."""
        monthly_payment: float = loan_amount * monthly_interest_rate / (1
        - 1 / (1 + monthly_interest_rate) ** (number_of_years * 12))
        return monthly_payment

    def compute_payment(self) -> None:  # try and except (ValueError)
        """Method for total payment calculation, it also displays the results."""
        try:
            monthly_payment: float = self.get_monthly_payment(
                float(self.entry_loan_amount.get()),
                float(self.entry_interest_rate.get()) / 1200,
                int(self.entry_number_years.get())
            )
            self.result_monthly_payment.config(
                text=f'{monthly_payment:.3f}')

            total_payment: float = monthly_payment * \
                            (int(self.entry_number_years.get()) * 12)
            self.result_total_payment.config(
                text=f'{total_payment:.3f}')
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values.")

    def on_close(self) -> None:
        """Method, that creates message box when user tries to close app."""
        exit_choice: bool = messagebox.askyesno(title='Exit window',
                                                message='Would you like to close the program?')
        if exit_choice:
            self.window.destroy()


def start_application():
    simple_loan_calc: LoanCalculatorApp = LoanCalculatorApp()
    return simple_loan_calc  # will return the application without starting the main loop.


if __name__ == "__main__":
    start_application().window.mainloop()