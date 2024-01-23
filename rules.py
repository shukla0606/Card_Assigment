# total revenue




import datetime


class FLAGS:
    GREEN = 1
    AMBER = 2
    RED = 0
    MEDIUM_RISK = 3  # diplay purpose only
    WHITE = 4  # data is missing for this field

# This is a already written for your reference
def latest_financial_index(data: dict):
    
    for index, financial in enumerate(data.get("financials")):
        if financial.get("nature") == "STANDALONE":
            return index
    return 0




def total_revenue(data: dict, financial_index):
   
    try:
        financial_data = data.get("financials", [])
        if financial_data:
            pnl = financial_data[financial_index].get("pnl", {})
            return pnl.get("lineItems", {}).get("net_revenue", 0)
        else:
            return 0
    except IndexError:
        return 0



def total_borrowing(data: dict, financial_index):
    
    try:
        financial_data = data.get("financials", [])
        if financial_data:
            bs = financial_data[financial_index].get("bs", {})
            total_borrowings = bs.get("liabilities", {}).get("long_term_borrowings", 0) + bs.get("liabilities", {}).get("short_term_borrowings", 0)
            total_revenue_value = total_revenue(data, financial_index)
            if total_revenue_value != 0:
                return total_borrowings / total_revenue_value
            else:
                return 0
        else:
            return 0
    except IndexError:
        return 0



def iscr(data: dict, financial_index):
   
    try:
        financial_data = data.get("financials", [])
        if financial_data:
            pnl = financial_data[financial_index].get("pnl", {})
            bs = financial_data[financial_index].get("bs", {})
            profit_before_interest_and_tax = pnl.get("lineItems", {}).get("profit_before_interest_and_tax", 0)
            interest_expenses = bs.get("liabilities", {}).get("interest", 0)
            return (profit_before_interest_and_tax + 1) / (interest_expenses + 1)
        else:
            return 0
    except IndexError:
        return 0



def iscr_flag(data: dict, financial_index):
   
    iscr_value = iscr(data, financial_index)
    if iscr_value >= 2:
        return FLAGS.GREEN
    else:
        return FLAGS.RED



def total_revenue_5cr_flag(data: dict, financial_index):
   
    total_revenue_value = total_revenue(data, financial_index)
    if total_revenue_value >= 50000000:
        return FLAGS.GREEN
    else:
        return FLAGS.RED



def borrowing_to_revenue_flag(data: dict, financial_index):
   
    borrowing_to_revenue_ratio = total_borrowing(data, financial_index)
    if borrowing_to_revenue_ratio <= 0.25:
        return FLAGS.GREEN
    else:
        return FLAGS.AMBER




