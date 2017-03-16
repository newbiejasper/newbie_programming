# 设置初值
set.seed(888)
r <- 0.05
segma <- 0.2
s_0 <- 1
T <- 1
N <- 2^8
dt <- 1/N
dw <- sqrt(dt) * rnorm(N, mean = 0, sd = 1)
w <- cumsum(dw)

s_true <- s_0 * exp((r - 1/2 * segma^2) * seq(dt, T, dt) + segma * w)

t1 <- c(0, seq(dt, T, dt))
s_true <- c(s_0, s_true)

# 数值模拟
R <- 2
Dt <- R * dt
L <- N/R
s_winer <- rep(0, (L + 1))
s_winer[1] <- s_0

for (j in 2:(L + 1)) {
    delta_winer <- sum(dw[(R * (j - 2) + 1):(R * (j - 1))])
    s_winer[j] <- s_winer[j - 1] + Dt * r * s_winer[j - 1] + segma * s_winer[j - 1] * delta_winer
}

t2 <- c(0, seq(Dt, T, Dt))

plot(t1, s_true, type = "l", col = "red", xlab = "t", ylab = "S(t)")
lines(t2, s_winer, col = "blue")
legend(c("topleft"), fill = c("red", "blue"), c("true", "euler"), bty = "n")



