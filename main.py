from tkinter import *


class LoanCalculatorApp:
    def __init__(self):
        window = Tk()
        window.geometry('550x350')
        window.title('Loan Calculator App')
        window.configure(background='#F1D7DA')

        Label(window, background='#F1D7DA', text='Annual Interest Rate: ',
              font=("Helvetica", 13)).grid(
              column=0, row=0, padx=10, pady=10, sticky='w')

        self.entry_interest_rate = Entry(window)  # not right column number
        self.entry_interest_rate.grid(column=1, row=0)

        Label(window, background='#F1D7DA', text='Number Of Years: ', font=("Helvetica", 13)).grid(
            column=0, row=1, padx=10, pady=10, sticky='w')

        self.entry_number_years = Entry(window)
        self.entry_number_years.grid(column=1, row=1)

        Label(window, background='#F1D7DA', text='Loan amount: ',
              font=("Helvetica", 13)).grid(column=0, row=2, padx=10, pady=10, sticky='w')

        self.entry_loan_amount = Entry(window)
        self.entry_loan_amount.grid(column=1, row=2)

        Label(window, background='#F1D7DA', text='Monthly Payment: ',
              font=("Helvetica", 13)).grid(column=0, row=3, padx=10, pady=10)

        Label(window, background='#F1D7DA', text='Total Payment: ',
              font=("Helvetica", 13)).grid(column=0, row=4, padx=10, pady=10)

        Button(window, text='Compute Payment', command=self.compute_payment,
               font=("Helvetica", 12), bg="#4CAF50", fg="white").grid(column=1, row=5)

        self.result_monthly_payment = Label(window, background='#F1D7DA', text='', font=("Helvetica", 14))
        self.result_monthly_payment.grid(column=1, row=3,
                                         padx=10, pady=10)

        self.result_total_payment = Label(window, background='#F1D7DA',
                                          text='', font=("Helvetica", 14))
        self.result_total_payment.grid(column=1, row=4,
                                       padx=10, pady=10)

        window.mainloop()

    def get_monthly_payment(self, loan_amount, monthly_interest_rate, number_of_years):  # надо исправить рассчет первый
        monthly_payment = loan_amount * monthly_interest_rate / (1
                                                                 - 1 / (1 + monthly_interest_rate) ** (
                                                                         number_of_years * 12))
        return monthly_payment

    def compute_payment(self):  # try and except (ValueError)
        monthly_payment = self.get_monthly_payment(
            float(self.entry_loan_amount.get()),
            float(self.entry_interest_rate.get()) / 1200,
            int(self.entry_number_years.get())
        )
        self.result_monthly_payment.config(
            text=f'Monthly Payment: {monthly_payment:.3f}')

        total_payment = monthly_payment * (int(self.entry_number_years.get()) * 12)
        self.result_total_payment.config(text=f'Total Payment: {total_payment:.3f}')


simple_loan_calc = LoanCalculatorApp()