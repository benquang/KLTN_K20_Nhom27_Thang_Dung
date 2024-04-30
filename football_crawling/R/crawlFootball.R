devtools::install_github("JaseZiv/worldfootballR")
library(worldfootballR)
library(dplyr)

countries <- c("ENG","FRA","ESP","ITA","GER")
seasons <- c(2018:2024)
# seasons<-c(2024)

parse <- function() {
    parse_on_country()
}
parse_on_country <- function() {
    for (country in countries)
    {
        parse_on_season(country = country)
    }

}
parse_on_season <- function(country) {
    for (i in seasons)
    {
        match_urls <- fb_match_urls(country = country, gender = "M", season_end_year = i, tier="1st")
        match_results <- fb_match_results(country = country, gender = "M", season_end_year = i, tier = "1st")
        write.csv(match_results, file = './fbref/match_results.csv', append = TRUE, row.names = FALSE)
        for (match_url in match_urls)
        {
            match_lineups <- fb_match_lineups(match_url = match_url)
            write.csv(match_lineups, file = './fbref/match_lineups.csv', append = TRUE, row.names = FALSE)
            match_summary<- fb_match_summary(match_url = match_url)
            write.csv(match_summary, file = './fbref/match_summary.csv', append = TRUE, row.names = FALSE)
            match_stats <- fb_team_match_stats(match_url = match_url)
            write.csv(match_stats, file = './fbref/match_stats.csv', append = TRUE, row.names = FALSE)
            advanced_match_stats <- fb_advanced_match_stats(match_url = match_url, stat_type = "summary", team_or_player = "team")
            write.csv(advanced_match_stats, file = './fbref/advanced_match_stats.csv', append = TRUE, row.names = FALSE)
        }
    }
}
main <- function() {
    parse()
}

# Call the main function
main()