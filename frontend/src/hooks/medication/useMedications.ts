import { Medication } from "@/utils/types/medication";
import { getMatchingMedications } from "./medicationApi";

const useMedications = () => {

    const getMedications = async (medicationName: string): Promise<Medication[] | null> => {
        if (!medicationName) { return null }
        const medication = await getMatchingMedications(medicationName)
        console.log(medication)
        return medication
    }

    return {
        getMedications
    }

}

export default useMedications