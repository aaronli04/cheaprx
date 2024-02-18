import styles from './ResultCard.module.css'
import { Medication } from '@/utils/types/medication'
import Link from 'next/link'


const ResultCard: React.FC<Medication> = (props: Medication) => {
  return (
    <div className={styles.liner}>
      <div className={styles.header}>
        <div className={styles.name}>
          {props.name}
        </div>
      </div>
      <div className={styles.info}>
        <div className={styles.position}>
          {props.price}
        </div>
        <div className={styles.company}>
          {props.generic}
        </div>
      </div>
      <div className={styles.buttonSection}>
        <Link href={props.link}>
          <button className={styles.interviewButton}>
            <div>
              Interview
            </div>
          </button>
        </Link>
      </div>
    </div>
  )
}

export default ResultCard