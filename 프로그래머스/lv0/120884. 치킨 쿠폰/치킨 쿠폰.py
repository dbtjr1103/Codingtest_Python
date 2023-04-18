def solution(chicken):
    coupon, service = chicken, 0
    
    while coupon >= 10:
        service += coupon // 10 
        coupon = coupon % 10 + coupon // 10
    
    return service + coupon // 10 