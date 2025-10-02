# Revenue Split Documentation

## Calculation Formulas

### Variables
- **V** - Transaction volume (amount)
- **F** - Platform fee rate (0 < F ≤ 1)
- **P** - Partner share percentage (0 ≤ P ≤ 1)
- **R** - Referral commission rate (0 ≤ R ≤ 1)

### Revenue Distribution Formulas
fee_total = V * F
partner_gross = fee_total * P
referral = partner_gross * R
partner_net = partner_gross - referral
platform_net = fee_total - partner_gross

### Calculation Steps
1. **Total Fee**: `fee_total = V × F`
   - Calculate total platform fee from transaction

2. **Partner Gross**: `partner_gross = fee_total × P`
   - Partner's share before referral deductions

3. **Referral Commission**: `referral = partner_gross × R`
   - Amount paid to referrer from partner's share

4. **Partner Net**: `partner_net = partner_gross - referral`
   - Partner's final earnings after referral payment

5. **Platform Net**: `platform_net = fee_total - partner_gross`
   - Platform's earnings after paying partner

### Example Calculation

**Input:**
- V = $1000
- F = 0.05 (5%)
- P = 0.30 (30%)
- R = 0.10 (10%)

**Calculation:**
fee_total = 1000 × 0.05 = $50.00
partner_gross = 50 × 0.30 = $15.00
referral = 15 × 0.10 = $1.50
partner_net = 15 - 1.50 = $13.50
platform_net = 50 - 15 = $35.00

### Validation Rules
- All calculations must be precise to the nearest cent
- Sum of all distributions must equal total fee: `fee_total = platform_net + partner_gross`
- Partner net must equal: `partner_net = partner_gross × (1 - R)`
