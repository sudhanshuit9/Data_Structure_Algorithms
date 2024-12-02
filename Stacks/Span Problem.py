#Find the stock span for each day (number of consecutive days the stock price was less than or equal to today's price).

def stock_span(prices):
    stack = []
    span = []

    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] <= price:
            stack.pop()
        span.append(i - stack[-1] if stack else i + 1)
        stack.append(i)

    return span

# Example Usage
prices = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(prices))
