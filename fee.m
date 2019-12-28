
function fee = fee(init) 
    if init < 10.99 
        fee = 0.99; 
    elseif init < 26.49
        fee = 1.49;
    elseif init < 51.99
        fee = 1.99; 
    else
        fee = 2.99;
    end
end  