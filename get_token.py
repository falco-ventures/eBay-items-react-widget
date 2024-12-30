import base64

# Original string
data = "FalcoVen-Instacar-PRD-6fa6592a8-05f9a277:PRD-fa6592a87a07-1071-4af4-bca9-68ce"

# Encode the string to bytes, then encode to Base64
encoded_bytes = base64.b64encode(data.encode('utf-8'))

# Convert the encoded bytes back to a string
encoded_str = encoded_bytes.decode('utf-8')

print(encoded_str)  # Output: RmFsY29WZW4tSW5zdGFjYXItUFJELTZmYTY1OTJhOC0wNWY5YTI3NzpQUkQtZmE2NTkyYTg3YTA3LTEwNzEtNGFmNC1iY2E5LTY4Y2U=
