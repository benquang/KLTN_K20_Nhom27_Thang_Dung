devtools::install_github("JaseZiv/worldfootballR")
library(worldfootballR)
library(dplyr)

# countries <- c("ENG","FRA","ESP","ITA","GER")
countries <- c("ESP")

# seasons <- c(2018)
seasons <- c(2018:2024)

parse <- function() {
    parse_on_country()
}
delete_all_files <- function() {
    file.remove('./ESP_fbref/match_results.csv')
    file.remove('./ESP_fbref/match_lineups.csv')
    file.remove('./ESP_fbref/match_summary.csv')
    file.remove('./ESP_fbref/match_stats.csv')
    file.remove('./ESP_fbref/advanced_match_stats.csv')
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
        write.table(match_results, file = './ESP_fbref/match_results.csv', append = TRUE, row.names = FALSE, sep = ",", col.names = !file.exists('./ESP_fbref/match_results.csv'))
        for (match_url in match_urls)
        {
            tryCatch(
                {
                    match_lineups <- fb_match_lineups(match_url = match_url)
                    write.table(match_lineups, file = './ESP_fbref/match_lineups.csv', append = TRUE, row.names = FALSE, sep = ",", col.names = !file.exists('./ESP_fbref/match_lineups.csv'))
                    match_summary<- fb_match_summary(match_url = match_url)
                    write.table(match_summary, file = './ESP_fbref/match_summary.csv', append = TRUE, row.names = FALSE, sep = ",", col.names = !file.exists('./ESP_fbref/match_summary.csv'))
                    match_stats <- fb_team_match_stats(match_url = match_url)
                    write.table(match_stats, file = './ESP_fbref/match_stats.csv', append = TRUE, row.names = FALSE, sep = ",", col.names = !file.exists('./ESP_fbref/match_stats.csv'))
                    advanced_match_stats <- fb_advanced_match_stats(match_url = match_url, stat_type = "summary", team_or_player = "team")
                    write.table(advanced_match_stats, file = './ESP_fbref/advanced_match_stats.csv', append = TRUE, row.names = FALSE, sep = ",", col.names = !file.exists('./ESP_fbref/advanced_match_stats.csv'))
                },
                error = function(e) {
                    print(paste("Error at URL:", match_url))
                    print(paste("Error: ", e))
                    print("\n")
                }
            )
        }
    }
}
main <- function() {
    parse()
}

# Call the main function
main()