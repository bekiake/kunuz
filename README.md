# kunuz
Kunuz Loyihasi 
% Boshlang'ich qiymatlar
X = [12, 2, 33, 3];
Y = [24, 4, 66, 6];

% O'rtacha qiymatlarni hisoblash
mean_X = mean(X);
mean_Y = mean(Y);

% Kovaryansni hisoblash
covariance = sum((X - mean_X) .* (Y - mean_Y)) / (length(X) - 1);

% Varianslarni hisoblash
var_X = sum((X - mean_X).^2) / (length(X) - 1);
var_Y = sum((Y - mean_Y).^2) / (length(Y) - 1);

% Korelyatsiya koeffitsientini hisoblash
correlation_coefficient = covariance / sqrt(var_X * var_Y);

% Natijani chiqarish
disp(['Kovaryansi: ' num2str(covariance)]);
disp(['X uchun varians: ' num2str(var_X)]);
disp(['Y uchun varians: ' num2str(var_Y)]);
disp(['Korelyatsiya koeffitsienti: ' num2str(correlation_coefficient)]);
