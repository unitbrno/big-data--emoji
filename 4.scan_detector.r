fw_data <- read.csv2("fwdata.csv")
fw_data$time <- as.POSIXct(fw_data$time, format="%m-%d-%H:%M:%S")

x <- table(cut(fw_data$time, breaks="min"))
print("Histogram of port scanning: ")
plot(x, type = "l")

y <- table(fw_data[, c("DPT", "DST")])
y[y > 0] = 1

z <- as.data.frame.matrix(y) 
abc <- colSums(z)
print("How many ports were scanned: ")
sort(abc, decreasing = T)
