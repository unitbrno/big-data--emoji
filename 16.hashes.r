library(stringr)

parseHashes <- function (input, output, nrows=1000) {
    x <- read.csv2(input, nrows=nrows)
    x <- x[grepl("Process", x$Message), ]
    y <- gsub("\\n+", ";", x$Message)
    y <- str_split_fixed(y, ";", 50)
    y <- gsub("\\S*:", "", y)
    y[18] <- gsub("\\s*SHA256=", "", y[18])
    y <- y[, c(6, 18)]
    y <- y[grepl("SHA256", y[, 2]), ]
    write.csv2(y, output)
}

parseHashes("PC1_sysmon.csv", "PC1_sysmon_hashes.csv")
parseHashes("PC5_sysmon.csv", "PC5_sysmon_hashes.csv")
parseHashes("PC6_sysmon.csv", "PC6_sysmon_hashes.csv")

