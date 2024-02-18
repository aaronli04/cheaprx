import styles from './HeaderSection.module.css'

const HeaderSection = () => {
    return (
        <div className={styles.liner}>
            <div className={styles.titleSection}>
                <div className={styles.title}>
                    <div className={styles.titleBlack}>
                        Cheap
                    </div>
                    <div className={styles.titleGreen}>
                        Rx
                    </div>
                </div>
                <div className={styles.subtitle}>
                    Find your cheapest drug.
                </div>
            </div>
        </div>
    )
}

export default HeaderSection