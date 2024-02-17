import Link from 'next/link'
import styles from './HeaderSection.module.css'

const HeaderSection = () => {
    return (
        <div className={styles.liner}>
            <div className={styles.titleSection}>
                <div className={styles.title}>
                    Find the Cheapest Price for Your Medication
                </div>
                <div className={styles.subtitle}>
                    Search across GoodRX, CostPlusDrugs, BlinkHealth, and others in seconds
                </div>
            </div>
        </div>
    )
}

export default HeaderSection