/* SELECT
// *
// FROM pysparkdbt.bronze.trips
*/

/*

SELECT * FROM {{ source('source_bronze', 'trips') }}
*/

SELECT * FROM {{ ref('trips') }}