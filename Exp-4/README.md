# Exp-4: Generate and Verify X.509 Self-Signed Digital Certificate

## Aim
To generate a self-signed X.509 certificate using OpenSSL on Windows, inspect its structure, and verify its validity.

## Theory
An X.509 certificate binds a public key to an identity. In a self-signed certificate, the issuer and subject are the same, and the certificate is signed using its own private key. This is useful for local testing and learning, but it is not trusted by default by browsers.

## Methodology

### 1. Generate a private key
```powershell
openssl genrsa -out private.key 2048
```

- `genrsa`: creates an RSA private key
- `-out private.key`: saves the key in a file named `private.key`
- `2048`: uses 2048-bit key length

### 2. Create a Certificate Signing Request (CSR)
```powershell
openssl req -new -key private.key -out request.csr
```

- `req`: creates a certificate request
- `-new`: generates a new CSR
- `-key private.key`: uses the generated private key
- `-out request.csr`: saves the request in `request.csr`

Enter details such as:
- Country: `IN`
- Common Name: `localhost`

### 3. Generate the self-signed certificate
```powershell
openssl x509 -req -days 365 -in request.csr -signkey private.key -out certificate.crt
```

- `x509`: works with X.509 certificates
- `-req`: reads a CSR as input
- `-days 365`: valid for 365 days
- `-signkey private.key`: signs using the same private key
- `-out certificate.crt`: saves the certificate

### 4. Decode and inspect the certificate
```powershell
openssl x509 -in certificate.crt -text -noout
```

This shows details such as:
- Subject
- Issuer
- Validity period
- Serial number
- Public key information
- Signature algorithm

### 5. Verify the certificate
```powershell
openssl verify -CAfile certificate.crt certificate.crt
```

If the certificate is valid, the result is:
```powershell
certificate.crt: OK
```

## Result
A private key and a self-signed X.509 certificate were created successfully. The certificate was decoded and verified using OpenSSL.

## Improvements
- Import to Windows Root Store: Import the generated certificate.crt into certmgr.msc under "Trusted Root Certification Authorities" to eliminate local Windows security alerts.
- Add Subject Alternative Name (SAN): Modern browsers on Windows reject certificates using only Common Name (CN); adding SAN extensions (subjectAltName) resolves browser warnings.
- Use CA-Signed Certificates: Transition to a trusted CA (e.g., Let’s Encrypt or an Active Directory Certificate Services CA) for enterprise production environments.

## Discussion
Self-signed certificates are useful for local development and testing, but they are not trusted by browsers or Windows systems unless imported into the trusted root store. For production, a CA-signed certificate is preferred.

## Conclusion
This experiment demonstrates how to generate, inspect, and verify a self-signed digital certificate using OpenSSL on Windows.
