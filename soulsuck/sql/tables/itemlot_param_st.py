from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import ITEMLOT_PARAM_ST


class ItemlotParamST(Base):
    __tablename__ = "itemlot_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    item1_id: Mapped[int]
    item2_id: Mapped[int]
    item3_id: Mapped[int]
    item4_id: Mapped[int]
    item5_id: Mapped[int]
    item6_id: Mapped[int]
    item7_id: Mapped[int]
    item8_id: Mapped[int]
    item1_category: Mapped[int]
    item2_category: Mapped[int]
    item3_category: Mapped[int]
    item4_category: Mapped[int]
    item5_category: Mapped[int]
    item6_category: Mapped[int]
    item7_category: Mapped[int]
    item8_category: Mapped[int]
    item1_chance_points: Mapped[int]
    item2_chance_points: Mapped[int]
    item3_chance_points: Mapped[int]
    item4_chance_points: Mapped[int]
    item5_chance_points: Mapped[int]
    item6_chance_points: Mapped[int]
    item7_chance_points: Mapped[int]
    item8_chance_points: Mapped[int]
    item1_cumulative_points: Mapped[int]
    item2_cumulative_points: Mapped[int]
    item3_cumulative_points: Mapped[int]
    item4_cumulative_points: Mapped[int]
    item5_cumulative_points: Mapped[int]
    item6_cumulative_points: Mapped[int]
    item7_cumulative_points: Mapped[int]
    item8_cumulative_points: Mapped[int]
    item1_flag: Mapped[int]
    item2_flag: Mapped[int]
    item3_flag: Mapped[int]
    item4_flag: Mapped[int]
    item5_flag: Mapped[int]
    item6_flag: Mapped[int]
    item7_flag: Mapped[int]
    item8_flag: Mapped[int]
    item_flag: Mapped[int]
    first_cumulative_flag: Mapped[int]
    max_cumulative_additions: Mapped[int]
    item_lot_rarity: Mapped[int]
    item1_count: Mapped[int]
    item2_count: Mapped[int]
    item3_count: Mapped[int]
    item4_count: Mapped[int]
    item5_count: Mapped[int]
    item6_count: Mapped[int]
    item7_count: Mapped[int]
    item8_count: Mapped[int]
    item1_luck_enabled: Mapped[bool]
    item2_luck_enabled: Mapped[bool]
    item3_luck_enabled: Mapped[bool]
    item4_luck_enabled: Mapped[bool]
    item5_luck_enabled: Mapped[bool]
    item6_luck_enabled: Mapped[bool]
    item7_luck_enabled: Mapped[bool]
    item8_luck_enabled: Mapped[bool]
    item1_reset_cumulative_points_on_drop: Mapped[bool]
    item2_reset_cumulative_points_on_drop: Mapped[bool]
    item3_reset_cumulative_points_on_drop: Mapped[bool]
    item4_reset_cumulative_points_on_drop: Mapped[bool]
    item5_reset_cumulative_points_on_drop: Mapped[bool]
    item6_reset_cumulative_points_on_drop: Mapped[bool]
    item7_reset_cumulative_points_on_drop: Mapped[bool]
    item8_reset_cumulative_points_on_drop: Mapped[bool]
    
    def __init__(self, id: int, source: ITEMLOT_PARAM_ST):
        self.id = id
        self.item1_id = source.Item1ID
        self.item2_id = source.Item2ID
        self.item3_id = source.Item3ID
        self.item4_id = source.Item4ID
        self.item5_id = source.Item5ID
        self.item6_id = source.Item6ID
        self.item7_id = source.Item7ID
        self.item8_id = source.Item8ID
        self.item1_category = source.Item1Category
        self.item2_category = source.Item2Category
        self.item3_category = source.Item3Category
        self.item4_category = source.Item4Category
        self.item5_category = source.Item5Category
        self.item6_category = source.Item6Category
        self.item7_category = source.Item7Category
        self.item8_category = source.Item8Category
        self.item1_chance_points = source.Item1ChancePoints
        self.item2_chance_points = source.Item2ChancePoints
        self.item3_chance_points = source.Item3ChancePoints
        self.item4_chance_points = source.Item4ChancePoints
        self.item5_chance_points = source.Item5ChancePoints
        self.item6_chance_points = source.Item6ChancePoints
        self.item7_chance_points = source.Item7ChancePoints
        self.item8_chance_points = source.Item8ChancePoints
        self.item1_cumulative_points = source.Item1CumulativePoints
        self.item2_cumulative_points = source.Item2CumulativePoints
        self.item3_cumulative_points = source.Item3CumulativePoints
        self.item4_cumulative_points = source.Item4CumulativePoints
        self.item5_cumulative_points = source.Item5CumulativePoints
        self.item6_cumulative_points = source.Item6CumulativePoints
        self.item7_cumulative_points = source.Item7CumulativePoints
        self.item8_cumulative_points = source.Item8CumulativePoints
        self.item1_flag = source.Item1Flag
        self.item2_flag = source.Item2Flag
        self.item3_flag = source.Item3Flag
        self.item4_flag = source.Item4Flag
        self.item5_flag = source.Item5Flag
        self.item6_flag = source.Item6Flag
        self.item7_flag = source.Item7Flag
        self.item8_flag = source.Item8Flag
        self.item_flag = source.ItemFlag
        self.first_cumulative_flag = source.FirstCumulativeFlag
        self.max_cumulative_additions = source.MaxCumulativeAdditions
        self.item_lot_rarity = source.ItemLotRarity
        self.item1_count = source.Item1Count
        self.item2_count = source.Item2Count
        self.item3_count = source.Item3Count
        self.item4_count = source.Item4Count
        self.item5_count = source.Item5Count
        self.item6_count = source.Item6Count
        self.item7_count = source.Item7Count
        self.item8_count = source.Item8Count
        self.item1_luck_enabled = source.Item1LuckEnabled
        self.item2_luck_enabled = source.Item2LuckEnabled
        self.item3_luck_enabled = source.Item3LuckEnabled
        self.item4_luck_enabled = source.Item4LuckEnabled
        self.item5_luck_enabled = source.Item5LuckEnabled
        self.item6_luck_enabled = source.Item6LuckEnabled
        self.item7_luck_enabled = source.Item7LuckEnabled
        self.item8_luck_enabled = source.Item8LuckEnabled
        self.item1_reset_cumulative_points_on_drop = source.Item1ResetCumulativePointsOnDrop
        self.item2_reset_cumulative_points_on_drop = source.Item2ResetCumulativePointsOnDrop
        self.item3_reset_cumulative_points_on_drop = source.Item3ResetCumulativePointsOnDrop
        self.item4_reset_cumulative_points_on_drop = source.Item4ResetCumulativePointsOnDrop
        self.item5_reset_cumulative_points_on_drop = source.Item5ResetCumulativePointsOnDrop
        self.item6_reset_cumulative_points_on_drop = source.Item6ResetCumulativePointsOnDrop
        self.item7_reset_cumulative_points_on_drop = source.Item7ResetCumulativePointsOnDrop
        self.item8_reset_cumulative_points_on_drop = source.Item8ResetCumulativePointsOnDrop