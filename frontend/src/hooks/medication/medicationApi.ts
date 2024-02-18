import { Medication } from "@/utils/types/medication";

const parseMedication = (medication: any): Medication[] | null => {
    return null
}

export const getMatchingMedications = async (medicationName: string): Promise<Medication[] | null> => {
    const response = await fetch(process.env.NEXT_PUBLIC_API_URL + '/api/medication', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            name: medicationName,
        }),
    })
    if (!response.ok) {
        throw new Error('Error occurred')
    }
    return parseMedication(await response.json())
}