
---

# **pystdf4**

**An object-oriented Python library for parsing and generating STDF (Standard Test Data Format) files used in semiconductor testing and manufacturing.**

---

## 🧩 Overview

**pystdf4** provides a modern, object-oriented interface for working with **STDF v4** files — the industry-standard binary data format for semiconductor test results.
It supports both **reading** and **writing** of STDF files, with a clean Python API that abstracts low-level binary details into high-level Pythonic objects.

---

## 📘 STDF4 Data Type Codes

The **Standard Test Data Format (STDF)** specification defines compact type codes to describe how values are stored and interpreted within records.
Each type code corresponds to a C data type, defining the byte layout and valid range of values.

| Code     | Description                                   | C Type Specifier | Notes                                                                    |
| :------- | :-------------------------------------------- | :--------------- | :----------------------------------------------------------------------- |
| `C*12`   | Fixed-length character string (12 characters) | `char[12]`       | Left-justified; pad with spaces if shorter than 12 characters.           |
| `C*n`    | Variable-length character string              | `char[]`         | First byte stores the length (0–255).                                    |
| `C*f`    | Variable-length string with external length   | `char[]`         | Length determined by another record field.                               |
| `U*1`    | 1-byte unsigned integer                       | `unsigned char`  | Range: 0–255                                                             |
| `U*2`    | 2-byte unsigned integer                       | `unsigned short` | Range: 0–65,535                                                          |
| `U*4`    | 4-byte unsigned integer                       | `unsigned long`  | Range: 0–4,294,967,295                                                   |
| `I*1`    | 1-byte signed integer                         | `char`           | Range: –128 to 127                                                       |
| `I*2`    | 2-byte signed integer                         | `short`          | Range: –32,768 to 32,767                                                 |
| `I*4`    | 4-byte signed integer                         | `long`           | Range: –2,147,483,648 to 2,147,483,647                                   |
| `R*4`    | 4-byte floating-point number (IEEE 754)       | `float`          | Standard single-precision float                                          |
| `R*8`    | 8-byte floating-point number (IEEE 754)       | `double`         | Standard double-precision float                                          |
| `B*6`    | Fixed-length binary field (6 bytes)           | `char[6]`        | Raw binary data                                                          |
| `V*n`    | Variable-type field                           | —                | First byte = type code, followed by up to 255 bytes of data              |
| `B*n`    | Variable-length binary field                  | `char[]`         | First byte = byte count (0–255); data starts at LSB of second byte       |
| `D*n`    | Variable-length bit field                     | `char[]`         | First two bytes = bit count (0–65,535); unused bits in last byte = 0     |
| `N*1`    | Nibble (4-bit) data                           | `char`           | Stores unsigned integers in 4-bit units; high nibble zeroed if odd count |
| `kxTYPE` | Array of specified data type                  | `TYPE[]`         | Length `k` determined by another record field (e.g. `kxU*2`)             |

---

## 🧱 PyStdf4 Data Model

The **PyStdf4 type system** provides a structured, extensible way to represent STDF data elements as Python classes.
Each class encapsulates type conversion, byte parsing, and STDF serialization.

```
StdfDataBase[T]  (Abstract Generic Base)
├── StdfIntBase     → U_1, U_2, U_4, I_1, I_2, I_4
├── StdfFloatBase   → R_4, R_8
├── StdfStringBase  → C_n, C_12
└── StdfBinaryBase  → B_n
```

These classes standardize how data flows between **Python**, **C-style internal representations**, and **STDF binary data**.

---

## 🔄 Data Flow

The transformation pipeline for STDF data in **pystdf4** can be summarized as follows:

```
py_value (Python type)
   ⇄ [build_py / parse_py]
internal_bytes (C-style binary data)
   ⇄ [build_stdf / parse_stdf]
stdf_value (STDF field data)
```

This design ensures each data element can:

* be **parsed** from STDF binary files,
* be **converted** into native Python types for analysis or manipulation,
* and be **re-serialized** back into valid STDF format.

---

## 🧪 Example Use Cases (Coming Soon)

* Parse STDF records into structured Python objects
* Convert STDF to human-readable CSV or JSON
* Build new STDF records programmatically
* Validate field encoding/decoding across STDF revisions

---

## 📜 License

MIT License © 2025
Developed for efficient and reliable STDF data manipulation in modern semiconductor workflows.

---

Would you like me to extend it with an **“Installation and Quick Start”** section (e.g., `pip install pystdf4` and a short usage example)? That would make it more complete for public release on GitHub or PyPI.
