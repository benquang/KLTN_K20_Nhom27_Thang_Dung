from datetime import datetime

class CustomFuncs:
    @staticmethod
    def UCM_convert_date(date_string):
        # Get the current year
        current_year = datetime.now().year
        # Parse the original date string
        date_obj = datetime.strptime(date_string, "%A %d %B")
        # Add the current year to the date object
        date_obj = date_obj.replace(year=current_year)
        # Format the date as "dd/mm/yyyy"
        formatted_date = date_obj.strftime("%Y-%m-%d")
        return formatted_date