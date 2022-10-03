class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = False

        a, b = a[::-1], b[::-1]

        for i in range(max(len(a),len(b))):
            digitA = a[i] if i < len(a) else "0"
            digitB = b[i] if i < len(b) else "0"

            if (digitA == "1") and (digitB == "1"):
                if carry:
                    res += "1"
                    carry = True
                else:
                    res += "0"
                    carry = True
            elif (digitA == "1") or (digitB == "1"):
                if carry:
                    res+="0"
                else:
                    res+="1"
                    carry = False
            else:
                if carry:
                    res+="1"
                    carry = False
                else:
                    res+="0"
        if carry:
            res+="1"

        return res[::-1]