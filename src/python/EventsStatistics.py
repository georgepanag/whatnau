

class EventsStatistics:

    def ChooseRegionAndTimePeriod(self,region,select_year_to_start,select_month_to_start,select_year_to_finish,select_month_to_finish):
        REGION=region
        SELECT_YEAR_TO_START=select_year_to_start
        SELECT_MONTH_TO_START=select_month_to_start
        SELECT_YEAR_TO_FINISH=select_year_to_finish
        SELECT_MONTH_TO_FINISH=select_month_to_finish

        List_of_cities = ["Athens", "Patras", "Kalamata", "Agrinio", "Messologgi", "Thessaloniki"]
        REGION = List_of_cities[0]  # select Athens
        print(REGION)
        select_year_to_start = ["2000", "2001", "2002", "2003", "2004", "2005","2006", "2007", "2008", "2009", "2010", "2011","2012", "2013", "2014", "2015", "2016", "2017","2018", "2019", "2020", "2021"]
        select_month_to_start = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
        select_year_to_finish = ["2000", "2001", "2002", "2003", "2004", "2005","2006", "2007", "2008", "2009", "2010", "2011","2012", "2013", "2014", "2015", "2016", "2017","2018", "2019", "2020", "2021"]
        select_month_to_finish = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]







EventsStatistics1 = EventsStatistics()

