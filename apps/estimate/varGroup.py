# SQLAlchemy 사용을 위한 var 그룹을 만들어두었음
user1 = "superpower"
pw1 = "mecha75"
ip1 = "192.168.0.10:63306"
# ip1 = "192.168.0.20"
db1 = "flaskbook"
mysql_url = f"mysql+pymysql://{user1}:{pw1}@{ip1}/{db1}?charset=utf8"

targetGroup=['CGS','GP','SalesExpences','OperatingProfit1','AdminExpences','OperatingProfit2',\
             'NonOperatingRevenue','NonOperatingEnpences','OrdinaryIncome1','OrdinaryIncome2',\
             'OrdinaryIncome3','OrdinaryIncome4','NetIncome']
tGroupName=['CGS(%)','GP(%)','SalesExpences(%)','OperatingProfit1(%)','AdminExpences(%)','OperatingProfit2(%)',\
            'NonOperatingRevenue(%)','NonOperatingEnpences(%)','OrdinaryIncome1(%)','OrdinaryIncome2(%)',\
            'OrdinaryIncome3(%)','OrdinaryIncome4(%)','NetIncome(%)']

costElementGroup = ['mm','company','Sales','CGS','CGM','Freight',\
                    'Insure_ex','GP','SalesExpences','Agent_ex','Agent_inland','Moving_ex',\
                    'Moving_inland','Insure_PL','Comp_ex','Comp_inland','Packing_ex',\
                    'Packing_inland','Royalty_inland','Royalty_ex','Advertisement_ex',\
                    'Advertisement_inland','OperatingProfit1','AdminExpences','SalaryBOD'\
                    ,'Salary','Pension','EmployBenefit','Travel','Telecommunication',\
                    'Utilities','TaxesAndDues','Rent','Depreciation','Amortization',\
                    'Maintanance','Insurance','Entertainment','SampleFee','TransportFee',\
                    'Commission','Service','BedDept','Consumable','Training','BooksAndPrinting',\
                    'Vehicle','Conference','Miscellaneous','Overseas','Warehouse',\
                    'ReversalBadDebt','ResearchDevelopment','LeaseAmortization','OperatingProfit2',\
                    'NonOperatingRevenue','FinancialRevenue','InterestRevenue',\
                    'TradingSecuritiesInterest','FxRevenue','FxRevenue_Operating','FxIncone_NonOp',\
                    'DerivativesRevenue','TradingSecuritiesRevenue','OtherNonOPRevenue',\
                    'DividentRevenue','MiscellaneousProfit','Gain_disposal_assets','Gain_OtherNonOP',\
                    'ReversalNRV','ReversalOtherAllowance','NonOperatingEnpences','FinancialCost',\
                    'Interest','BondInterest','LossDisposalAR','FxLoss','FxLoss_Operating',\
                    'FxLoss_NonOP','DerivativesLoss_tot','DerivativesLoss','TradingSecuritiesLoss',\
                    'OtherNonOPLoss','Donation','Loss_disposal_assets','Loss_disposal_inventory',\
                    'Loss_OtherNonOP','MiscellaneousLoss','OtherAllowance','OrdinaryIncome1',\
                    'Gain_disposal_assets_NonOP','DebtForgiveness','LeaseInterestIncome',\
                    'OtherSpecialGain','Loss_disposal_assets_NonOP','DebtForgivenessAmortization',\
                    'LeaseInterestCost','OtherSpecialLoss','ValuationLoss','OrdinaryIncome2',\
                    'FxValuation','FxValuationGain_OP','FxValuationGain_NonOP','FxValuationLoss_OP',\
                    'FxValuationLoss_NonOP','DerivativesVauation','DerivativesVauationGain',\
                    'DerivativesVauationLoss','OrdinaryIncome3','SecuritiesGain','SecuritiesLoss',\
                    'OrdinaryIncome4','Tax','NetIncome','user_id','create_at']

costElementGroup2 = ['Sales','CGS','CGS(%)','CGM','Freight',\
                    'Insure_ex','GP','GP(%)','SalesExpences','SalesExpences(%)','Agent_ex','Agent_inland','Moving_ex',\
                    'Moving_inland','Insure_PL','Comp_ex','Comp_inland','Packing_ex',\
                    'Packing_inland','Royalty_inland','Royalty_ex','Advertisement_ex',\
                    'Advertisement_inland','OperatingProfit1','OperatingProfit1(%)',\
                    'AdminExpences','AdminExpences(%)','SalaryBOD'\
                    ,'Salary','Pension','EmployBenefit','Travel','Telecommunication',\
                    'Utilities','TaxesAndDues','Rent','Depreciation','Amortization',\
                    'Maintanance','Insurance','Entertainment','SampleFee','TransportFee',\
                    'Commission','Service','BedDept','Consumable','Training','BooksAndPrinting',\
                    'Vehicle','Conference','Miscellaneous','Overseas','Warehouse',\
                    'ReversalBadDebt','ResearchDevelopment','LeaseAmortization',\
                    'OperatingProfit2','OperatingProfit2(%)','NonOperatingRevenue','NonOperatingRevenue(%)',\
                    'FinancialRevenue','InterestRevenue','TradingSecuritiesInterest','FxRevenue',\
                    'FxRevenue_Operating','FxIncone_NonOp',\
                    'DerivativesRevenue','TradingSecuritiesRevenue','OtherNonOPRevenue',\
                    'DividentRevenue','MiscellaneousProfit','Gain_disposal_assets','Gain_OtherNonOP',\
                    'ReversalNRV','ReversalOtherAllowance','NonOperatingEnpences','NonOperatingEnpences(%)',\
                    'FinancialCost','Interest','BondInterest','LossDisposalAR','FxLoss','FxLoss_Operating',\
                    'FxLoss_NonOP','DerivativesLoss_tot','DerivativesLoss','TradingSecuritiesLoss',\
                    'OtherNonOPLoss','Donation','Loss_disposal_assets','Loss_disposal_inventory',\
                    'Loss_OtherNonOP','MiscellaneousLoss','OtherAllowance','OrdinaryIncome1','OrdinaryIncome1(%)',\
                    'Gain_disposal_assets_NonOP','DebtForgiveness','LeaseInterestIncome',\
                    'OtherSpecialGain','Loss_disposal_assets_NonOP','DebtForgivenessAmortization',\
                    'LeaseInterestCost','OtherSpecialLoss','ValuationLoss','OrdinaryIncome2',\
                    'FxValuation','FxValuationGain_OP','FxValuationGain_NonOP','FxValuationLoss_OP',\
                    'FxValuationLoss_NonOP','DerivativesVauation','DerivativesVauationGain',\
                    'DerivativesVauationLoss','OrdinaryIncome3','SecuritiesGain','SecuritiesLoss',\
                    'OrdinaryIncome4','OrdinaryIncome4(%)','Tax','NetIncome','NetIncome(%)']

costLabel = {'Sales':[0,'1. 매출액',''],'CGS':[0,'2. 매출원가',''],'CGM':[2,'매출원가',''],'Freight':[3,'선임',''],\
             'Insure_ex':[4,'수출보험료',''],'GP':[0,'3. 매출총이익',''],'SalesExpences':[0,'4. 판매직접비',''],\
             'Agent_ex':[2,'수출수수료',''],'Agent_inland':[3,'내수판매수수료',''],'Moving_ex':[3,'수출운반비',''],\
             'Moving_inland':[3,'내수운반비',''],'Insure_PL':[3,'P. L. 보험료',''],'Comp_ex':[3,'수출교환보상비',''],\
             'Comp_inland':[3,'내수교환보상비',''],'Packing_ex':[3,'수출포장비',''],\
             'Packing_inland':[3,'내수포장비',''],'Royalty_inland':[3,'내수상표사용료',''],\
             'Royalty_ex':[3,'수출상표사용료',''],'Advertisement_ex':[3,'해외광고선전비',''],\
             'Advertisement_inland':[4,'국내광고선전비',''],'OperatingProfit1':[0,'5. 영업이익①',''],\
             'AdminExpences':[0,'6. 일반관리비',''],'SalaryBOD':[2,'임원급여',''],'Salary':[3,'급료와 수당',''],\
             'Pension':[3,'퇴직충당금',''],'EmployBenefit':[3,'복리후생비',''],'Travel':[3,'여비교통비',''],\
             'Telecommunication':[3,'통신비',''],'Utilities':[3,'수도광열비',''],'TaxesAndDues':[3,'세금과공과',''],\
             'Rent':[3,'지급임차료',''],'Depreciation':[3,'감가상각비',''],'Amortization':[3,'무형자산상각',''],\
             'Maintanance':[3,'수선비',''],'Insurance':[3,'보험료',''],'Entertainment':[3,'접대비',''],\
             'SampleFee':[3,'견본비',''],'TransportFee':[3,'기타운반비',''],'Commission':[3,'지급수수료',''],\
             'Service':[3,'관리용역비',''],'BedDept':[3,'대손상각비',''],'Consumable':[3,'소모품비',''],\
             'Training':[3,'교육훈련비',''],'BooksAndPrinting':[3,'도서인쇄비',''],'Vehicle':[3,'차량유지비',''],\
             'Conference':[3,'회의비',''],'Miscellaneous':[3,'잡비',''],'Overseas':[3,'해외지사경비',''],\
             'Warehouse':[3,'창고관리비',''],'ReversalBadDebt':[3,'대손상각비 환입',''],\
             'ResearchDevelopment':[3,'시험연구비',''],'LeaseAmortization':[4,'리스상각비',''],\
             'OperatingProfit2':[0,'8. 영업이익②',''],'NonOperatingRevenue':[0,'9. 영업외수익',''],\
             'FinancialRevenue':[2,'9.1. 금융수익',''],'InterestRevenue':[3,'이자수익',''],\
             'TradingSecuritiesInterest':[3,'단기매매증권이자수익',''],'FxRevenue':[3,'9.2. 외환차익',''],\
             'FxRevenue_Operating':[3,'외환차익(영업)',''],'FxIncone_NonOp':[3,'외환차익(비영업)',''],\
             'DerivativesRevenue':[3,'9.3. 파생상품거래이익',''],'TradingSecuritiesRevenue':[3,'단기매매증권처분이익',''],\
             'OtherNonOPRevenue':[3,'9.4. 기타영업외수익',''],'DividentRevenue':[3,'배당금수익',''],\
             'MiscellaneousProfit':[3,'잡이익',''],'Gain_disposal_assets':[3,'유형자산처분이익',''],\
             'Gain_OtherNonOP':[3,'기타영업외이익',''],'ReversalNRV':[3,'재고자산평가충당금환입',''],\
             'ReversalOtherAllowance':[4,'기타대손충당금환입',''],'NonOperatingEnpences':[0,'10. 영업외비용',''],\
             'FinancialCost':[2,'10.1. 금융비용',''],'Interest':[3,'이자비용',''],'BondInterest':[3,'사채이자',''],\
             'LossDisposalAR':[3,'매출채권매각손실',''],'FxLoss':[3,'10.2. 외환차손',''],\
             'FxLoss_Operating':[3,'외환차손(영업)',''],'FxLoss_NonOP':[3,'외환차손(비영업)',''],\
             'DerivativesLoss_tot':[3,'10.3. 파생상품거래손실',''],'DerivativesLoss':[3,'파생상품거래손실',''],\
             'TradingSecuritiesLoss':[3,'단기매매증권처분손실',''],'OtherNonOPLoss':[3,'10.4. 기타영업외비용',''],\
             'Donation':[3,'기부금',''],'Loss_disposal_assets':[3,'유형자산처분손실',''],\
             'Loss_disposal_inventory':[3,'재고자산폐기손실',''],'Loss_OtherNonOP':[3,'기타영업외비용',''],\
             'MiscellaneousLoss':[3,'잡손실',''],'OtherAllowance':[4,'기타대손상각비',''],\
             'OrdinaryIncome1':[0,'11. 경상이익①',''],'Gain_disposal_assets_NonOP':[2,'유형자산처분이익(비경상)',''],\
             'DebtForgiveness':[3,'채무면제이익',''],'LeaseInterestIncome':[3,'리스이자수익',''],\
             'OtherSpecialGain':[3,'기타특별영업외수익',''],'Loss_disposal_assets_NonOP':[3,'유형자산처분손실(비경상)',''],\
             'DebtForgivenessAmortization':[3,'채무면제상각이자',''],'LeaseInterestCost':[3,'리스이자비용',''],\
             'OtherSpecialLoss':[3,'기타특별영업외손실',''],'ValuationLoss':[4,'유/무형감액손실,리스처분손실',''],\
             'OrdinaryIncome2':[0,'12. 경상이익②',''],'FxValuation':[2,'12.1. 외화환산손익',''],\
             'FxValuationGain_OP':[3,'외화환산이익(영업)',''],'FxValuationGain_NonOP':[3,'외화환산이익(비영업)',''],\
             'FxValuationLoss_OP':[3,'외화환산손실(영업)',''],'FxValuationLoss_NonOP':[3,'외화환산손실(비영업)',''],\
             'DerivativesVauation':[3,'12.2. 파생(보증채무)평가손익',''],'DerivativesVauationGain':[3,'파생상품평가이익',''],\
             'DerivativesVauationLoss':[4,'파생상품평가손실',''],'OrdinaryIncome3':[0,'13. 경상이익③',''],\
             'SecuritiesGain':[2,'투자유가증권평가이익',''],'SecuritiesLoss':[4,'투자유가증권평가손실',''],\
             'OrdinaryIncome4':[0,'14. 경상이익④',''],'Tax':[3,'15. 법인세비용',''],'NetIncome':[0,'16. 당기순이익',''],\
             'CGS(%)':[1,'매출원가(%)','%'],'GP(%)':[0,'매출총이익(%)','%'],'SalesExpences(%)':[1,'판매직접비(%)','%'],\
             'OperatingProfit1(%)':[0,'영업이익1(%)','%'],'AdminExpences(%)':[1,'일반관리비(%)','%'],\
             'OperatingProfit2(%)':[0,'영업이익2(%)','%'],'NonOperatingRevenue(%)':[1,'영업외수익(%)','%'],\
             'NonOperatingEnpences(%)':[1,'영업외비용(%)','%'],'OrdinaryIncome1(%)':[0,'경상이익1(%)','%'],\
             'OrdinaryIncome2(%)':[1,'경상이익2(%)','%'],'OrdinaryIncome3(%)':[1,'경상이익3(%)','%'],\
             'OrdinaryIncome4(%)':[0,'경상이익4(%)','%'],'NetIncome(%)':[0,'당기순이익(%)','%']}

company_code = {
    '1000':['Consolidated','KRW'],
    '1100':['HQ','KRW'],
    '2100':['KTS','CNY'],
    '2200':['NKT','CNY'],
    '2300':['KTT','CNY'],
    '2400':['KTC','CNY'],
    '2500':['Hongkong','USD'],
    '3100':['Japan','JPY'],
    '3300':['KTV','USD'],
    '5100':['Germany','EUR'],
    '5200':['UK','GBP'],
    '5300':['France','EUR'],
    '6100':['KUSA','USD'],
    '6200':['Canada','CAD'],
    '6300':['KTG','USD'],
    '7100':['Cairo','USD'],
    '8100':['Maxico','MXN'],
    '9100':['Australia','AUD'],
    '9900':['Total','KRW'],
    '-100':['Eliminated','KRW']
}

other_input = {
'매출원가':'CGM',
'선임':'Freight',
'수출보험료':'Insure_ex',
'수출수수료':'Agent_ex',
'내수판매수수료':'Agent_inland',
'수출운반비':'Moving_ex',
'내수운반비':'Moving_inland',
'P. L. 보험료':'Insure_PL',
'수출교환보상비':'Comp_ex',
'내수교환보상비':'Comp_inland',
'수출포장비':'Packing_ex',
'내수포장비':'Packing_inland',
'내수상표사용료':'Royalty_inland',
'수출상표사용료':'Royalty_ex',
'해외광고선전비':'Advertisement_ex',
'국내광고선전비':'Advertisement_inland',
'급료와 수당':'Salary',
'해외지사경비':'Overseas',
'창고관리비':'Warehouse',
'시험연구비':'ResearchDevelopment'
}

# 개별 항목 입력 후 계산필드를 채우기 위한 변수
order_cal_lv1 = {
    'CGS':[
    'CGM',
    'Freight',
    'Insure_ex'
    ],
    'SalesExpences':[
    'Agent_ex',
    'Agent_inland',
    'Moving_ex',
    'Moving_inland',
    'Insure_PL',
    'Comp_ex',
    'Comp_inland',
    'Packing_ex',
    'Packing_inland',
    'Royalty_inland',
    'Royalty_ex',
    'Advertisement_ex',
    'Advertisement_inland'
    ],
    'AdminExpences':[
    'SalaryBOD',
    'Salary',
    'Pension',
    'EmployBenefit',
    'Travel',
    'Telecommunication',
    'Utilities',
    'TaxesAndDues',
    'Rent',
    'Depreciation',
    'Amortization',
    'Maintanance',
    'Insurance',
    'Entertainment',
    'SampleFee',
    'TransportFee',
    'Commission',
    'Service',
    'BedDept',
    'Consumable',
    'Training',
    'BooksAndPrinting',
    'Vehicle',
    'Conference',
    'Miscellaneous',
    'Overseas',
    'Warehouse',
    'ReversalBadDebt',
    'ResearchDevelopment',
    'LeaseAmortization'
    ],
    'FinancialRevenue':[
    'InterestRevenue',
    'TradingSecuritiesInterest'    
    ],
    'FxRevenue':[
    'FxRevenue_Operating',
    'FxIncone_NonOp'    
    ],
    'DerivativesRevenue':['TradingSecuritiesRevenue'],
    'OtherNonOPRevenue':[
    'DividentRevenue',
    'MiscellaneousProfit',
    'Gain_disposal_assets',
    'Gain_OtherNonOP',
    'ReversalNRV',
    'ReversalOtherAllowance'    
    ],
    'FinancialCost':[
    'Interest',
    'BondInterest',
    'LossDisposalAR'    
    ],
    'FxLoss':[
    'FxLoss_Operating',
    'FxLoss_NonOP'    
    ],
    'DerivativesLoss_tot':[
    'DerivativesLoss',
    'TradingSecuritiesLoss'    
    ],
    'OtherNonOPLoss':[
    'Donation',
    'Loss_disposal_assets',
    'Loss_disposal_inventory',
    'Loss_OtherNonOP',
    'MiscellaneousLoss',
    'OtherAllowance'    
    ],
    'Gain_disposal_assets_NonOP':[
    'DebtForgiveness',
    'LeaseInterestIncome',
    'OtherSpecialGain'
    ],
    'Loss_disposal_assets_NonOP':[
    'DebtForgivenessAmortization',
    'LeaseInterestCost',
    'OtherSpecialLoss',
    'ValuationLoss'        
    ],
    'NonOperatingRevenue':[
    'FinancialRevenue',
    'FxRevenue',
    'DerivativesRevenue',
    'OtherNonOPRevenue'        
    ],
    'NonOperatingEnpences':[
    'FinancialCost',
    'FxLoss',
    'DerivativesLoss_tot',
    'OtherNonOPLoss'        
    ]
}

order_cal_lv2 = {
    'GP':
    [['+','Sales'],
    ['-','CGS']],
    'OperatingProfit1':
    [['+','GP'],
    ['-','SalesExpences']],
    'OperatingProfit2':
    [['+','OperatingProfit1'],
    ['-','AdminExpences']],
    'OrdinaryIncome1':
    [['+','OperatingProfit2'],
    ['+','NonOperatingRevenue'],
    ['-','NonOperatingEnpences']],
    'OrdinaryIncome2':
    [['+','OrdinaryIncome1'],
    ['+','Gain_disposal_assets_NonOP'],
    ['-','Loss_disposal_assets_NonOP']],
    'FxValuation':
    [['+','FxValuationGain_OP'],
    ['+','FxValuationGain_NonOP'],
    ['-','FxValuationLoss_OP'],
    ['-','FxValuationLoss_NonOP']],
    'DerivativesVauation':
    [['+','DerivativesVauationGain'],
    ['-','DerivativesVauationLoss']],
    'OrdinaryIncome3':
    [['+','OrdinaryIncome2'],
    ['+','FxValuation'],
    ['-','DerivativesVauation']],
    'OrdinaryIncome4':
    [['+','OrdinaryIncome3'],
    ['+','SecuritiesGain'],
    ['-','SecuritiesLoss']],
    'NetIncome':
    [['+','OrdinaryIncome4'],
    ['-','Tax']]
}