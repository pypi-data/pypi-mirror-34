#pragma once
#include "common.hpp"

namespace CPU {
    // Interrupt type
    enum IntType { NMI, RESET, IRQ, BRK };
    // Addressing mode
    typedef u16 (*Mode)(void);

    /* Processor flags */
    enum Flag {C, Z, I, D, V, N};
    class Flags {
        // a private data structure to hold the flags
        bool f[6];

    public:

        /** Handle accessing this object using brackets */
        bool& operator[] (const int i) { return f[i]; }

        /** Return the flags as a byte */
        u8 get() {
            return f[C] |
                f[Z] << 1 |
                f[I] << 2 |
                f[D] << 3 |
                1 << 5 |
                f[V] << 6 |
                f[N] << 7;
        }

        /** Set the flags from a full byte */
        void set(u8 p) {
            f[C] = NTH_BIT(p, 0);
            f[Z] = NTH_BIT(p, 1);
            f[I] = NTH_BIT(p, 2);
            f[D] = NTH_BIT(p, 3);
            f[V] = NTH_BIT(p, 6);
            f[N] = NTH_BIT(p, 7);
        }

    };

    u8 read_mem(u16 address);
    void write_mem(u16 address, u8 value);
    void set_nmi(bool v = true);
    void set_irq(bool v = true);
    void power();
    void run_frame();
}
