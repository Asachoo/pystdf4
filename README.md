# pystdf4
An object-oriented Python library for parsing and generating STDF (Standard Test Data Format) files used in semiconductor testing and manufacturing.

## STDF4 Data Type Codes and Meanings

The Standard Test Data Format (STDF) specification defines a concise set of data type codes for representing values within STDF records. These codes determine how data is stored and interpreted.

| Code     | Description                                   | C Type Specifier           | Notes |
| :------- | :-------------------------------------------- | :------------------------- | :---- |
| `C*12`   | Fixed-length character string (12 characters) | `char[12]`                 | Must be left-justified and padded with spaces if not fully populated. |
| `C*n`    | Variable-length character string              | `char[]`                   | First byte is an unsigned count (0-255) of the following data bytes. |
| `C*f`    | Variable-length character string              | `char[]`                   | Length is specified by another field in the record. |
| `U*1`    | One-byte unsigned integer                     | `unsigned char`            | Range: 0 to 255. |
| `U*2`    | Two-byte unsigned integer                     | `unsigned short`           | Range: 0 to 65,535. |
| `U*4`    | Four-byte unsigned integer                    | `unsigned long`            | Range: 0 to 4,294,967,295. |
| `I*1`    | One-byte signed integer                       | `char`                     | Range: -128 to 127. |
| `I*2`    | Two-byte signed integer                       | `short`                    | Range: -32,768 to 32,767. |
| `I*4`    | Four-byte signed integer                      | `long`                     | Range: -2,147,483,648 to 2,147,483,647. |
| `R*4`    | Four-byte floating-point number (IEEE 754)    | `float`                    | Standard single-precision float. |
| `R*8`    | Eight-byte floating-point number (IEEE 754)   | `double` (`long float`)    | Standard double-precision float. |
| `B*6`    | Fixed-length bit-encoded data (6 bytes)       | `char[6]`                  | Raw binary data. |
| `V*n`    | Variable data type field                      |                            | First byte is a data type code, followed by data (max 255 bytes). |
| `B*n`    | Variable-length bit-encoded field             | `char[]`                   | First byte is an unsigned count (0-255) of following data bytes. Data starts in the least significant bit of the second byte. |
| `D*n`    | Variable-length bit-encoded field             | `char[]`                   | First two bytes are an unsigned count (0-65,535) of bits. Data starts in the least significant bit of the third byte. Unused high bits in the last byte must be zero. |
| `N*1`    | Nibble (4-bit) data                           | `char`                     | Stores unsigned integers. First item in low 4 bits, second in high 4 bits. If odd count, high nibble of the last byte is zero. |
| `kxTYPE` | Array of a specified data type                | `TYPE[]`                   | `k` (number of elements) is defined by an earlier field in the record, e.g., `kxU*2`. |

---
