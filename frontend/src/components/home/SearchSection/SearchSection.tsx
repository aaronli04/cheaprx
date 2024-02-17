import styles from './SearchSection.module.css'

const SearchSection = () => {
    return (
        <div className={styles.liner}>
            <div className={styles.searchSection}>
                <div className={styles.titleSection}>
                    <div className={styles.title}>
                        Find your cheapest drug.
                    </div>
                </div>
            </div>
        </div>
    )
}

export default SearchSection