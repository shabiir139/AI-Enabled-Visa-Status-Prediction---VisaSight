'use client';

import React from 'react';
import styles from './StatsCard.module.css';

interface StatsCardProps {
    title: string;
    value: string | number;
    subtitle?: string;
    icon: React.ReactNode;
    trend?: { value: number; isPositive: boolean };
    variant?: 'default' | 'primary' | 'success' | 'warning' | 'danger';
}

// ⚡ Bolt: Wrapped with React.memo to prevent unnecessary re-renders when parent dashboard components
// update states that don't affect this purely presentational component.
// Expected Impact: Eliminates redundant DOM diffing for stats cards during frequent parent re-renders.
const StatsCard = React.memo(function StatsCard({ title, value, subtitle, icon, trend, variant = 'default' }: StatsCardProps) {
    return (
        <div className={`${styles.card} ${styles[variant]}`}>
            <div className={styles.iconContainer}>{icon}</div>
            <div className={styles.content}>
                <span className={styles.title}>{title}</span>
                <span className={styles.value}>{value}</span>
                {subtitle && <span className={styles.subtitle}>{subtitle}</span>}
                {trend && (
                    <div className={`${styles.trend} ${trend.isPositive ? styles.positive : styles.negative}`}>
                        <span>{trend.isPositive ? '↑' : '↓'}</span>
                        <span>{Math.abs(trend.value)}%</span>
                    </div>
                )}
            </div>
        </div>
    );
});

export default StatsCard;
