# myapp/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('titre', 'type_news', 'date', 'time', 'view_on_streamlit', 'view_on_power_bi')

    def view_on_streamlit(self, obj):
        return format_html('<a href="{}" target="_blank">Go to Streamlit</a>', 'https://da-test-fdfovkkqk8nhmsvajzh7je.streamlit.app/')
    
    view_on_streamlit.short_description = 'Go to Streamlit'

    def view_on_power_bi(self, obj):
        return format_html('<a href="{}" target="_blank">Go to Power BI</a>', 'https://app.powerbi.com/links/m_GgtayceK?ctid=5c2fe400-c7db-4007-85f5-30119c0b1189&pbi_source=linkShare')
    
    view_on_power_bi.short_description = 'Go to Power BI'
