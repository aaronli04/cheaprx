'use client'
import styles from './ResultCard.module.css'
import { Medication } from '@/utils/types/medication'
import Link from 'next/link'
import { Button } from '@mantine/core'

const ResultCard: React.FC<Medication> = (props: Medication) => {
    return (
        <div className={styles.liner}>
            <div className={styles.header}>
                <div className={styles.name}>
                    {props.generic ?
                        props.name + ` (Generic for ${props.generic})` :
                        props.name
                    }
                </div>
                {props.prescriptionNeeded ?
                    <div className={styles.prescription}>
                        *Prescription Required
                    </div> :
                    null
                }
            </div>
            <div className={styles.info}>
                <div className={styles.buySection}>
                    <div>
                        {props.supplier} sells {props.name} for <span className={styles.price}>${props.price}</span>.
                    </div>
                    <div className={styles.buttonSection}>
                        <Link target="_blank" href={props.link}>
                            <Button
                                classNames={{
                                    root: styles.buttonRoot,
                                }}
                            >
                                Buy
                            </Button>
                        </Link>
                    </div>
                </div>
                <div>
                    {props.strength ?
                        props.strength + ', ' + props.count :
                        props.count
                    }
                </div>
            </div>
        </div>
    )
}

export default ResultCard