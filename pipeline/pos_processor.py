import pandas as pd


class POSProcessor:

    def __init__(
        self,
        csv_path
    ):

        self.df = pd.read_csv(
            csv_path
        )

    def purchase_count(self):

        return len(
            self.df
        )

    def total_revenue(self):

        amount_columns = [

            c
            for c in self.df.columns

            if "amount"
            in c.lower()
        ]

        if not amount_columns:
            return 0

        return float(
            self.df[
                amount_columns[0]
            ].sum()
        )