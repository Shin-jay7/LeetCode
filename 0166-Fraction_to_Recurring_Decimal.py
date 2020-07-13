from __future__ import annotations


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = "-" if numerator*denominator < 0 else ""
        result = [sign+str(n), "."]
        remainders = {}

        while remainder > 0 and remainder not in remainders:
            remainders[remainder] = len(result)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))

        if remainder in remainders:
            idx = remainders[remainder]
            result.insert(idx, "(")
            result.append(")")

        return "".join(result).rstrip(".") # Remove period if the text ends with period.
        # print("".join(result).rstrip("."))

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator%denominator == 0:
            return str(numerator//denominator)
            # print(str(numerator//denominator))
            # return

        p, q = map(abs, (numerator, denominator))
        prefix = ("" if numerator*denominator > 0 else "-") + str(p//q) + "."
        suffix = ""
        remainder = p%q
        remainders = {}

        while remainder not in remainders:
            remainders[remainder] = len(suffix)
            suffix += str(remainder*10//q)
            remainder = remainder*10%q
            if remainder == 0:
                return prefix+suffix
                # print(prefix+suffix)
                # return

        return prefix + suffix[:remainders[remainder]] + "(" + suffix[remainders[remainder]:] + ")"
        # print(prefix + suffix[:remainders[remainder]] + "(" + suffix[remainders[remainder]:] + ")")


test = Solution()
test.fractionToDecimal(1,2) # "0.5"

test = Solution()
test.fractionToDecimal(2,1) # "2"

test = Solution()
test.fractionToDecimal(2,3) # "0.(6)"
