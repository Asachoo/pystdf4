# **📦 pystdf4**

A modern, high-performance Python library for creating and parsing **STDF (Standard Test Data Format) v4** files used throughout semiconductor test and manufacturing.

---

## **🔍 Overview**

**pystdf4** offers a clean, Pythonic, and object-oriented interface for working with **STDF v4**, the industry-standard binary format for semiconductor test data.
It abstracts away low-level byte handling and record encoding, allowing engineers to focus on data modeling rather than binary protocol details.

With **pystdf4**, you can efficiently:

- **Generate STDF v4 files** using structured Python objects
- Build records using a robust and extensible field/record system
- Work with a high-performance dynamic byte buffer optimized for large datasets
- Integrate easily into automated test, analysis, and data processing pipelines

Support for **STDF file parsing (reader API)** is actively under development and coming soon.

---

## 📘 STDF4 Data Type Codes

The **Standard Test Data Format (STDF)** specification defines a compact set of type codes that describe how values are stored and interpreted within records.
Each type code corresponds to a C data type and specifies its binary layout, size, and valid range.

For a complete and authoritative description of all STDF v4 data types, please refer to the official STDF specification included in this repository (pystdf4/doc/stdf-spec.pdf).
The type code definitions summarized below correspond to the material on page 10 of the specification.

| Code     | Description                                   | C Type Specifier | Notes                                                                    |
| :------- | :-------------------------------------------  | :--------------- | :----------------------------------------------------------------------- |
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
FieldBase(pyT) (ABC)
├── ImmediateField(pyT)
│   ├── C_1     # fixed-length char (1 byte)
│   ├── B_1     # fixed-length binary (1 byte)
│   ├── C_n     # Pascal string (1-byte length + bytes)
│   └── B_n     # Pascal binary (1-byte length + bytes)
│
├── DeferredField(pyT)
│   ├── U_1     # uint8
│   ├── U_2     # uint16
│   ├── U_4     # uint32
│   ├── I_1     # int8
│   ├── I_2     # int16
│   ├── I_4     # int32
│   ├── R_4     # float32
│   └── R_8     # float64
│
├── ❌ C_f  (Pascal string with external length)
├── ❌ V_n  (typed variable field: <type><data>)
├── ❌ D_n  (bitstring with leading bit-count)
├── ❌ N_1  (nibble array 4-bit)
│
└── ❌ SequenceField
    ├── ❌ FixLenField       # fixed-size arrays, 如 B*6
    ├── ❌ VarLenField       # variable arrays with Pascal length
    └── ❌ KxLenField        # array with external length (k×TYPE)
        ├── ❌ KxU_1
        ├── ❌ KxU_2
        ├── ❌ KxC_n
        └── ❌ KxR_4
```

These classes standardize how data flows between **Python**, **C-style internal representations**, and **STDF binary data**.

---

## 📋 STDF v4 Record Types Implementation Status

| Record Type | Name                              | REC_TYP | REC_SUB | Status        | Notes                            |
| ----------- | --------------------------------- | ------- | ------- | ------------- | -------------------------------- |
| FAR         | File Attributes Record            | 0       | 10      | ✔️ Complete   | Required as first record         |
| ATR         | Audit Trail Record                | 0       | 20      | ✔️ Complete   | Tracks file modifications        |
| MIR         | Master Information Record         | 1       | 10      | ✔️ Complete   | Lot-level information            |
| MRR         | Master Results Record             | 1       | 20      | ✔️ Complete   | End of lot summary               |
| PCR         | Part Count Record                 | 1       | 30      | ✔️ Complete   | Part statistics                  |
| HBR         | Hardware Bin Record               | 1       | 40      | ✔️ Complete   | Physical binning counts          |
| SBR         | Software Bin Record               | 1       | 50      | ✔️ Complete   | Logical binning counts           |
| PMR         | Pin Map Record                    | 1       | 60      | ✔️ Complete   | Pin/channel mapping              |
| PGR         | Pin Group Record                  | 1       | 62      | ❌ Incomplete | Pin grouping                     |
| PLR         | Pin List Record                   | 1       | 63      | ❌ Incomplete | Pin group display properties     |
| RDR         | Retest Data Record                | 1       | 70      | ❌ Incomplete | Retest information               |
| SDR         | Site Description Record           | 1       | 80      | ✔️ Complete   | Test site configuration          |
| WIR         | Wafer Information Record          | 2       | 10      | ✔️ Complete   | Wafer start marker               |
| WRR         | Wafer Results Record              | 2       | 20      | ✔️ Complete   | Wafer completion summary         |
| WCR         | Wafer Configuration Record        | 2       | 30      | ✔️ Complete   | Wafer dimensions/orientation     |
| PIR         | Part Information Record           | 5       | 10      | ✔️ Complete   | Part start marker                |
| PRR         | Part Results Record               | 5       | 20      | ✔️ Complete   | Part completion results          |
| TSR         | Test Synopsis Record              | 10      | 30      | ✔️ Complete   | Test execution statistics        |
| PTR         | Parametric Test Record            | 15      | 10      | ✔️ Complete   | Single parametric test result    |
| MPR         | Multiple-Result Parametric Record | 15      | 15      | ❌ Incomplete | Multiple parametric test results |
| FTR         | Functional Test Record            | 15      | 20      | ❌ Incomplete | Functional test results          |
| BPS         | Begin Program Section Record      | 20      | 10      | ✔️ Complete   | Program section start marker     |
| EPS         | End Program Section Record        | 20      | 20      | ✔️ Complete   | Program section end marker       |
| GDR         | Generic Data Record               | 50      | 10      | ❌ Incomplete | User-defined data                |
| DTR         | Datalog Text Record               | 50      | 30      | ❌ Incomplete | Datalog comments                 |

---

## 🧪 Example Use Cases (Coming Soon)

- Parse STDF records into structured Python objects
- Convert STDF to human-readable CSV or JSON
- Build new STDF records programmatically
- Validate field encoding/decoding across STDF revisions

---

## 📜 License

MIT License © 2025
Developed for efficient and reliable STDF data manipulation in modern semiconductor workflows.
