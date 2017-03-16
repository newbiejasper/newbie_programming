T <- 1
N <- 500
dt <- T/N

dw <- rep(0, N)
w <- rep(0, N)

dw[1] <- sqrt(dt) * rnorm(1, mean = 0, sd = 1)
w[1] <- dw[1]

for (j in 2:N) {
    dw[j] <- sqrt(dt) * rnorm(1, mean = 0, sd = 1)
    w[j] <- w[j - 1] + dw[j]
}

plot(seq(0, 1, dt), c(0, w), type = "l", xlab = "t", ylab = "W(t)")
