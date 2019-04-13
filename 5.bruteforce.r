pc1_sec <- read.csv2("PC1_security.csv")
#pc1_app <- read.csv2("PC1_application.csv")
#pc1_sysmon <- read.csv2("PC1_sysmon.csv")
#pc1_system <- read.csv2("PC1_system.csv")

myplot <- function(x) {
    dates <- as.POSIXct(x$TimeCreated, format="%d.%m.%Y %H:%M:%S")

    x <- table(cut(dates, breaks="min"))
    plot(x, type = "l")
}

myplot(pc1_sec)
#myplot(pc1_app)
#myplot(pc1_sysmon)
#myplot(pc1_system)

mytable <- function(x) {
    dates <- as.POSIXct(x$TimeCreated, format="%d.%m.%Y %H:%M:%S")

    table(cut(dates, breaks="min"))
}

pc1secdates <- mytable(pc1_sec)
#pc1appdates <- mytable(pc1_app)
#pc1sysmondates <- mytable(pc1_sysmon)
#pc1systemdates <- mytable(pc1_system)

head(sort(pc1secdates, decreasing = T))
#head(sort(pc1appdates, decreasing = T))
#head(sort(pc1sysmondates, decreasing = T))
#head(sort(pc1systemdates, decreasing = T))
