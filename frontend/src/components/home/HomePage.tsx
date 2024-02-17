import styles from './page.module.css'
import HeaderSection from './HeaderSection/HeaderSection'
import SearchSection from './SearchSection/SearchSection'

const HomePage = () => {
  return (
    <div className={styles.liner}>
      <HeaderSection />
      <SearchSection />
    </div>
  )
}

export default HomePage