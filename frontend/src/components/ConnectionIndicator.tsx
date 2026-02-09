'use client';

import { useEffect, useState } from 'react';
import { connectionManager } from '@/lib/api';
import styles from './ConnectionIndicator.module.css';

type ConnectionState = 'connected' | 'connecting' | 'disconnected';

export default function ConnectionIndicator() {
    const [state, setState] = useState<ConnectionState>('disconnected');
    const [visible, setVisible] = useState(false);

    useEffect(() => {
        const unsubscribe = connectionManager.subscribe((newState) => {
            setState(newState);
            // Show indicator when connecting or disconnected
            setVisible(newState !== 'connected');
        });

        return unsubscribe;
    }, []);

    if (!visible) return null;

    return (
        <div className={`${styles.indicator} ${styles[state]}`}>
            <span className={styles.dot}></span>
            <span className={styles.text}>
                {state === 'connecting' ? 'Connecting to server...' : 'Server offline'}
            </span>
        </div>
    );
}
