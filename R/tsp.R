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

delta_distance <- function(city, m, n) {
    city[145, ] <- city[1, ]
    city_change <- city
    city_change[146, ] <- city_change[m, ]
    city_change[147, ] <- city_change[n, ]
    city_change[n, ] <- city_change[146, ]
    city_change[m, ] <- city_change[147, ]
    
    if (m == 1) {
        a1 <- sqrt(sum((city[1, ] - city[2, ])^2))
        b1 <- sqrt(sum((city[n, ] - city[n - 1, ])^2)) + sqrt(sum((city[n, ] - city[n + 1, 
            ])^2))
        a2 <- sqrt(sum((city_change[1, ] - city_change[2, ])^2))
        b2 <- sqrt(sum((city_change[n, ] - city_change[n - 1, ])^2)) + sqrt(sum((city_change[n, 
            ] - city_change[n + 1, ])^2))
    } else {
        if (n == 1) {
            a1 <- sqrt(sum((city[1, ] - city[2, ])^2))
            b1 <- sqrt(sum((city[m, ] - city[m - 1, ])^2)) + sqrt(sum((city[m, ] - city[m + 
                1, ])^2))
            a2 <- sqrt(sum((city_change[1, ] - city_change[2, ])^2))
            b2 <- sqrt(sum((city_change[m, ] - city_change[m - 1, ])^2)) + sqrt(sum((city_change[m, 
                ] - city_change[m + 1, ])^2))
        } else {
            a1 <- sqrt(sum((city[m, ] - city[m - 1, ])^2)) + sqrt(sum((city[m, ] - city[m + 
                1, ])^2))
            b1 <- sqrt(sum((city[n, ] - city[n - 1, ])^2)) + sqrt(sum((city[n, ] - city[n + 
                1, ])^2))
            a2 <- sqrt(sum((city_change[m, ] - city_change[m - 1, ])^2)) + sqrt(sum((city_change[m, 
                ] - city_change[m + 1, ])^2))
            b2 <- sqrt(sum((city_change[n, ] - city_change[n - 1, ])^2)) + sqrt(sum((city_change[n, 
                ] - city_change[n + 1, ])^2))
        }
    }
    return(a2 + b2 - a1 - b1)
}

initial_city <- city
for (T in seq(100, 0.01, -5)) {
    print(T)
    for (j in 1:30000) {
        start_city <- initial_city
        
        city_change <- start_city
        # 生成的两个整数是不是可以一样,这里首先选择不放回
        m <- sample(1:144, size = 2, replace = FALSE)
        city_change[146, ] <- city_change[m[1], ]
        city_change[147, ] <- city_change[m[2], ]
        city_change[m[2], ] <- city_change[146, ]
        city_change[m[1], ] <- city_change[147, ]
        
        u <- runif(1)
        if (u < min(1, exp(-delta_distance(start_city, m[1], m[2])/T))) {
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
