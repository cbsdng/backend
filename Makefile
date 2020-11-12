.include <name.py>

USE_FREENIT = YES
SERVICE != echo ${app_name}
REGGAE_PATH := /usr/local/share/reggae
SYSPKG := YES


celery: up
	@sudo cbsd jexec jname=${SERVICE} user=devel env SYSPKG=${SYSPKG} OFFLINE=${OFFLINE} /usr/src/bin/celery_devel.sh


.include <${REGGAE_PATH}/mk/service.mk>
