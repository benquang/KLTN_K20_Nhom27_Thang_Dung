devtools::install_github("JaseZiv/worldfootballR")
library(worldfootballR)
library(dplyr)

# countries <- c("ENG","FRA","ESP","ITA","GER")
countries <- c("ENG")

seasons <- c(2019:2024)
# seasons <- c(2018:2024)

parse <- function() {
    parse_on_country()
}
delete_all_files <- function() {
    file.remove('./fbref/match_results.csv')
    file.remove('./fbref/match_lineups.csv')
    file.remove('./fbref/match_summary.csv')
    file.remove('./fbref/match_stats.csv')
    file.remove('./fbref/advanced_match_stats.csv')
}
parse_on_country <- function() {
    delete_all_files()
    for (country in countries)
    {
        parse_on_season(country = country)
    }

}
shuffle_match_urls <- function(match_urls) {
    shuffled_urls <- sample(match_urls)
    return(shuffled_urls)
}
parse_on_season <- function(country) {
    for (i in seasons)
    {
        match_urls <- fb_match_urls(country = country, gender = "M", season_end_year = i, tier="1st")
        match_urls <- shuffle_match_urls(match_urls)
        match_results <- fb_match_results(country = country, gender = "M", season_end_year = i, tier = "1st")
        write.table(match_results, file = './fbref/match_results.csv', append = TRUE, row.names = FALSE, sep = ",", col.names = !file.exists('./fbref/match_results.csv'))
        for (match_url in match_urls)
        {
            match_lineups <- fb_match_lineups(match_url = match_url)
            write.table(match_lineups, file = './fbref/match_lineups.csv', append = TRUE, row.names = FALSE, sep = ",", col.names = !file.exists('./fbref/match_lineups.csv'))
            match_summary<- fb_match_summary(match_url = match_url)
            write.table(match_summary, file = './fbref/match_summary.csv', append = TRUE, row.names = FALSE, sep = ",", col.names = !file.exists('./fbref/match_summary.csv'))
            match_stats <- fb_team_match_stats(match_url = match_url)
            write.table(match_stats, file = './fbref/match_stats.csv', append = TRUE, row.names = FALSE, sep = ",", col.names = !file.exists('./fbref/match_stats.csv'))
            advanced_match_stats <- fb_advanced_match_stats(match_url = match_url, stat_type = "summary", team_or_player = "team")
            write.table(advanced_match_stats, file = './fbref/advanced_match_stats.csv', append = TRUE, row.names = FALSE, sep = ",", col.names = !file.exists('./fbref/advanced_match_stats.csv'))
        }
    }
}
main <- function() {
    parse()
}

# Call the main function
main()