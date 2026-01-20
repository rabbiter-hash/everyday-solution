
function compareEnergy(caloriesBurned, wattHoursUsed){
    /* ==============================================
        // 注释：
            比较运动过程中人体的卡里路消耗更多还是该次运动过程中电子设备消耗的能量更多
            为方便比较，将单位都转成焦耳(joules)
        ============================================== */
    if(caloriesBurned < 0 || wattHoursUsed < 0){
        console.warn("Input Must be positive!");
    }

    const workOutEnergy = caloriesBurned * 4184;
    const deviceEnergy = wattHoursUsed * 3600;

    if(workOutEnergy > deviceEnergy) {
        return "Workout";
    } else if(workoutEnergy < deviceEnergy) {
        return "Devices";
    } else {
        return "Equal";
    }
}