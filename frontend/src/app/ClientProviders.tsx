'use client';

import { ConnectionIndicator } from '@/components';

export default function ClientProviders({ children }: { children: React.ReactNode }) {
    return (
        <>
            <ConnectionIndicator />
            {children}
        </>
    );
}
