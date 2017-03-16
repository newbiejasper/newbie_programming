city <- read.table(file = "chn144.dat")
city <- city[, 2:3]
city[, 2] <- -city[, 2]

distance <- function(city) {
    city[145, ] <- city[1, ]
    a <- 0
    for (i in 1:144) {
        a <- a + sqrt((city[i, 1] - city[(i + 1), 1])^2 + (city[i, 2] - city[(i + 1), 2])^2)
    }
    return(a)
}

delta_distance <- function(city, m) {
    city[145, ] <- city[1, ]
    city_change <- city
    city_change[min(m):max(m), ] <- city_change[max(m):min(m), ]
    a <- min(m)
    b <- max(m)
    
    if (a == 1) {
        a1 <- 0
        b1 <- sqrt(sum((city[b, ] - city[b + 1, ])^2))
        a2 <- 0
        b2 <- sqrt(sum((city_change[b, ] - city_change[b + 1, ])^2))
    } else {
        a1 <- sqrt(sum((city[a, ] - city[(a - 1), ])^2))
        b1 <- sqrt(sum((city[b, ] - city[b + 1, ])^2))
        a2 <- sqrt(sum((city_change[a, ] - city_change[(a - 1), ])^2))
        b2 <- sqrt(sum((city_change[b, ] - city_change[(b + 1), ])^2))
    }
    return(a2 + b2 - a1 - b1)
}

initial_city <- city


for (T in seq(200, 0.01, -2)) {
    print(T)
    for (j in 1:20000) {
        start_city <- initial_city
        
        city_change <- start_city
        # 生成的两个整数是不是可以一样,这里首先选择不放回
        m <- sample(1:144, size = 2, replace = FALSE)
        
        city_change[min(m):max(m), ] <- city_change[max(m):min(m), ]
        
        u <- runif(1)
        if (u < min(1, exp(-delta_distance(start_city, m)/T))) {
            initial_city <- city_change
        } else {
            initial_city <- start_city
        }
    }
}

city <- initial_city
plot(city[, 1], city[, 2], xlim = c(0, 5000), ylim = c(-4000, 0), xlab = "", ylab = "", type = "n")

city[145, ] <- city[1, ]
for (i in 1:144) {
    lines(c(city[i, 1], city[(i + 1), 1]), c(city[i, 2], city[(i + 1), 2]))
}

distance(city)
