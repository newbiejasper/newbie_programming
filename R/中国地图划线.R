city <- read.table(file = "chn144.dat")
city <- city[, 2:3]
city[, 2] <- -city[, 2]

plot(city[, 1], city[, 2], xlim = c(0, 5000), ylim = c(-4000, 0), xlab = "", ylab = "", pch = 20)

distance <- 0
city[145, ] <- city[1, ]
for (i in 1:144) {
    lines(c(city[i, 1], city[(i + 1), 1]), c(city[i, 2], city[(i + 1), 2]))
    distance <- distance + sqrt((city[i, 1] - city[(i + 1), 1])^2 + (city[i, 2] - city[(i + 
        1), 2])^2)
}



# 结果是67511.77 36419.02 初始温度100 37665.12 35564.3 200 34927.55 500
