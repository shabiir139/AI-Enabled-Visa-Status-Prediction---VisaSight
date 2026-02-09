'use client';

import { useState, useEffect, useCallback } from 'react';
import { api } from '@/lib/api';
import styles from './ModelSelector.module.css';

interface ModelInfo {
    name: string;
    version: string;
    type: string;
    trained_at?: string;
    metrics?: Record<string, number | null>;
    is_active: boolean;
}

export default function ModelSelector() {
    const [models, setModels] = useState<ModelInfo[]>([]);
    const [loading, setLoading] = useState(true);
    const [switching, setSwitching] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [retryCount, setRetryCount] = useState(0);

    const fetchModels = useCallback(async (isRetry = false) => {
        setError(null);
        if (!isRetry) setLoading(true);

        try {
            const data = await api.models.list();
            setModels(data);
            setRetryCount(0);
        } catch (err) {
            console.error('Failed to fetch models:', err);

            // Auto-retry up to 3 times for cold starts
            if (retryCount < 3) {
                setRetryCount(prev => prev + 1);
                setError(`Connecting to server... (attempt ${retryCount + 1}/3)`);
                setTimeout(() => fetchModels(true), 2000);
                return;
            }

            setError('Failed to load models. Make sure the backend is running.');
        } finally {
            if (!isRetry || retryCount >= 3) {
                setLoading(false);
            }
        }
    }, [retryCount]);

    useEffect(() => {
        fetchModels();
    }, []);

    const switchModel = async (modelType: string) => {
        setSwitching(true);
        setError(null);
        try {
            await api.models.switch(modelType);
            await fetchModels();
        } catch (err) {
            console.error('Failed to switch model:', err);
            setError('Failed to switch model');
        } finally {
            setSwitching(false);
        }
    };

    if (loading) {
        return (
            <div className={styles.container}>
                <div className={styles.loading}>
                    <div className={styles.loadingSpinner}></div>
                    <span>{retryCount > 0 ? `Connecting to server... (attempt ${retryCount}/3)` : 'Loading models...'}</span>
                </div>
            </div>
        );
    }

    if (error && models.length === 0) {
        return (
            <div className={styles.container}>
                <div className={styles.error}>
                    <span>⚠️</span>
                    <span>{error}</span>
                    <button onClick={() => { setRetryCount(0); fetchModels(); }} className={styles.retryBtn}>
                        Retry
                    </button>
                </div>
            </div>
        );
    }

    return (
        <div className={styles.container}>
            <h3 className={styles.title}>🧠 AI Model Selection</h3>
            <p className={styles.subtitle}>Choose the prediction model</p>

            {error && (
                <div className={styles.errorBanner}>
                    {error}
                </div>
            )}

            <div className={styles.modelGrid}>
                {models.map((model) => (
                    <div
                        key={model.version}
                        className={`${styles.modelCard} ${model.is_active ? styles.active : ''}`}
                        onClick={() => !model.is_active && !switching && switchModel(model.type)}
                    >
                        <div className={styles.modelHeader}>
                            <span className={styles.modelIcon}>
                                {model.type === 'hf' ? '🤖' : model.type.startsWith('baseline') ? (model.type === 'baseline-xgb' ? '🚀' : '🌲') : '🎭'}
                            </span>
                            <span className={styles.modelName}>{model.name}</span>
                        </div>

                        <div className={styles.modelMeta}>
                            <span className={styles.version}>{model.version}</span>
                            {model.trained_at && (
                                <span className={styles.date}>
                                    Trained: {new Date(model.trained_at).toLocaleDateString()}
                                </span>
                            )}
                        </div>

                        {model.metrics && Object.keys(model.metrics).some(k => model.metrics?.[k] != null) && (
                            <div className={styles.metrics}>
                                {Object.entries(model.metrics)
                                    .filter(([, val]) => val != null)
                                    .map(([key, val]) => (
                                        <div key={key} className={styles.metric}>
                                            <span className={styles.metricLabel}>{key}</span>
                                            <span className={styles.metricValue}>
                                                {typeof val === 'number' ? val.toFixed(3) : val}
                                            </span>
                                        </div>
                                    ))}
                            </div>
                        )}

                        {model.is_active && (
                            <div className={styles.activeTag}>✓ Active</div>
                        )}

                        {switching && !model.is_active && (
                            <div className={styles.switchingOverlay}>
                                <div className={styles.loadingSpinner}></div>
                                <span>Switching...</span>
                            </div>
                        )}
                    </div>
                ))}
            </div>
        </div>
    );
}
