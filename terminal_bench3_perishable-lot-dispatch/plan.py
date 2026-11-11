def total_materials(orders):
    totals={}
    for order in orders:
        for material,qty in order['materials'].items(): totals[material]=totals.get(material,0)+qty
    return totals

def solve(request):
    return {'selected': [], 'schedule': [], 'reservations': []}
