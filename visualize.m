%% Visualize graph of profit on bitcoin                 

init_buy_price = 7340.30;
init_purchase = 70.00;
num_btc = (init_purchase - fee(init_purchase)) / init_buy_price;

final_sell_price = 7400.00;
final_sell = final_sell_price * num_btc;
final_sell - fee(final_sell) - init_purchase


syms x y
% X = final_sell_price
% Y = profit

% x * num_btc - fee(x * num_btc) - init_purchase
fzero(@(x) x * num_btc - fee(x * num_btc) - init_purchase, 7400)
figure(1)
fimplicit(@(x, y) x * (y - fee(y)) / init_buy_price - fee(x * (y - fee(y)) / init_buy_price) - y)
axis([5000 10000 5000 10000])
