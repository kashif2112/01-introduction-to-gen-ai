UPDATE extensions.langchain_pg_embedding
SET cmetadata = jsonb_set(
    cmetadata,
    '{team_name}',   -- 👈 missing comma was here
    to_jsonb(
        CASE cmetadata->>'team_name'
            WHEN 'Business Intelligence' THEN 'Business Intelligence Services'
            WHEN 'Vertex AI' THEN 'AI&ML Services - GenAI'
            WHEN 'Augment & HelpBot' THEN 'AI&ML Services - GenAI'
            WHEN 'DATABASE_AS_A_SERVICE' THEN 'Database As a Service'
            WHEN 'DATA_PROTECTION' THEN 'Data Protection Services'
            WHEN 'INFRA_MIDDLEWARE' THEN 'Infra Middleware Services'
            WHEN 'SONIC_STORAGE' THEN 'Sonic Storage Services'
            WHEN 'DATA_IN_MOTION' THEN 'Data In Motion'
        END
    ),
    false
)
WHERE cmetadata->>'team_name' IN (
    'Business Intelligence',
    'Vertex AI',
    'Augment & HelpBot',
    'DATABASE_AS_A_SERVICE',
    'DATA_PROTECTION',
    'INFRA_MIDDLEWARE',
    'SONIC_STORAGE',
    'DATA_IN_MOTION'
);


SELECT DISTINCT cmetadata->>'teamname' AS teamname
FROM your_table
WHERE cmetadata ? 'teamname';
